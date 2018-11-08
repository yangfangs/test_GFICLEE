from collections import Counter

import numpy as np
from itertools import islice
import scipy.spatial.distance as dist
import pandas as pd
import os
import multiprocessing
import numpy as np
from sklearn.metrics import normalized_mutual_info_score, adjusted_mutual_info_score, mutual_info_score


class GetPredict(object):
    def __init__(self,
                 profile_path,
                 out_path,
                 method):
        self.all_input_gene_path = None
        self.profile_path = profile_path
        self.out_path = out_path
        self.method = method

        self.profile = {}
        self.input_genes = {}
        self.input_genes_names = None
        self.input_genes_labels = None
        self.input_genes_data = None
        self.profile_names = None
        self.profile_data = None
        self.leave_path = None
        self.is_entrez = False


        if not os.path.isdir(self.out_path):
            os.makedirs(self.out_path)

    def leave_half(self, input_file_path, leave_file_path, pathway):

        if not os.path.isdir(input_file_path):
            os.makedirs(input_file_path)
        if not os.path.isdir(leave_file_path):
            os.makedirs(leave_file_path)

        input_genes = pd.read_csv(pathway, sep='\t')
        col_names = input_genes.columns[1]
        pathway = list(input_genes[col_names].unique())

        for i in range(len(pathway)):
            df = input_genes[input_genes[col_names].isin([pathway[i]])]
            for j in range(2):
                # get samples
                if df.shape[0] <= 2:
                    continue
                sample_num = round(df.shape[0] / 2)
                df_w = df.sample(sample_num,random_state=j)
                # leave out genes
                df_leave_out = df.drop(df_w.axes[0])

                # leave gene names
                file_name = '{0}_{1}.txt'.format(i, j)
                df_input_file = os.path.join(input_file_path, file_name)
                df_leave_file = os.path.join(leave_file_path, file_name)

                df_w.to_csv(df_input_file, sep='\t', index=False)
                df_leave_out.to_csv(df_leave_file, sep='\t', index=False)
        self.all_input_gene_path = input_file_path
        self.leave_path = leave_file_path




    def read_matrix(self, matrix_path: "The profile path") -> dict:
        """
        Read input gene profile matrix
        """

        with open(matrix_path) as f:
            for i in islice(f, 1, None):
                node = i.strip().split('\t')
                if self.is_entrez:
                    self.profile[node[0]] = list(map(int, node[2:]))
                else:
                    self.profile[node[1]] = list(map(int, node[2:]))


    def read_input(self, label_path: "The path to input gene") -> dict:

        """
        Read label
        """

        global node
        with open(label_path) as f:
            for i in islice(f, 1, None):
                node = i.strip().split('\t')
                self.input_genes[node[0]] = node[1]
        if node[0].isnumeric():
            self.is_entrez = True

    def prepare_data(self):
        self.read_matrix(self.profile_path)

        """
        Prepare input date for k-means and k-nn
        """
        labels_l = []
        data_l = []
        names_l = []
        profile_data = []
        profile_name = []
        for k, v in self.input_genes.items():
            names_l.append(k)
            labels_l.append(v)
            data_l.append(self.profile[k])
        self.input_genes_labels = np.array(labels_l)
        self.input_genes_data = np.array(data_l)
        self.input_genes_names = np.array(names_l)

        for key, value in self.profile.items():
            profile_name.append(key)
            profile_data.append(value)
        self.profile_names = np.array(profile_name)
        self.profile_data = np.array(profile_data)

    def pre_predict(self):

        dis = dist.cdist(self.profile_data, self.input_genes_data, self.method)

        # get min
        result = dis.min(axis=1)
        # get 25%
        # result = np.percentile(dis, 25, axis=1)
        dic = {'name': list(self.profile_names), 'score': list(result)}
        pre = pd.DataFrame(dic)
        return pre
    def entropy(self,labels):
        prob_dict = Counter(labels)
        s = sum(prob_dict.values())
        probs = np.array([i/s for i in prob_dict.values()])
        return -probs.dot(np.log(probs))
    def mi_score(self,a,b):
        a_b = ["{0}{1}".format(i,j) for i,j in zip(a,b)]
        return self.entropy(a) + self.entropy(b) - self.entropy(a_b)

    def pre_mutual_info(self):
        all_res = []
        for i in self.input_genes_data:
            all_pre = []
            for j in self.profile_data:
                all_pre.append(self.mi_score(i, j))
            all_res.append(all_pre)
        all_res_np = np.array(all_res)
        all_res_max = all_res_np.max(axis=0)
        dic = {'name': list(self.profile_names), 'score': list(all_res_max)}
        pre = pd.DataFrame(dic)
        return pre

    def run_pre(self,input_file):
        print(input_file)
        input_path = self.all_input_gene_path
        input_file_name = os.path.join(input_path, input_file)
        output_path = self.out_path
        output_file_name = os.path.join(output_path, input_file)
        self.read_input(input_file_name)
        self.prepare_data()
        # re = self.pre_predict()
        if self.method == "mutual_info":
            re = self.pre_mutual_info()
            re = re.sort_values('score', ascending=False)

        else:
            re = self.pre_predict()
            re = re.sort_values('score', ascending=True)

        re.to_csv(output_file_name, sep='\t', index=False)


    def run(self,core):
        tasks = list(filter(lambda f: not f.startswith('.'), os.listdir(self.all_input_gene_path)))
        # tasks = check_task(all_input_genes_file)
        cores = core
        pool = multiprocessing.Pool(processes=cores)
        pool.map(self.run_pre, tasks)



if __name__ == '__main__':
    foo = GetPredict()
    foo.read_matrix('/home/yangfang/PCSF/clime_roc/all_kegg_matrix_re111.txt')

    def check_task(num):
        check_result = []
        all_input_gene_path = '/home/yangfang/PCSF/no_report/test_re111/input'
        for i in num:
            f = os.path.join(all_input_gene_path, i)
            if os.path.getsize(f) != 30:
                check_result.append(i)
        return check_result


    def run_pre(input_file):
        input_path = '/home/yangfang/PCSF/no_report/test_re111/input'
        input_file_name = os.path.join(input_path, input_file)
        output_path = '/home/yangfang/PCSF/hamming_roc/hamming_kegg/'
        output_file_name = os.path.join(output_path, input_file)
        foo.read_input(input_file_name)
        foo.prepare_data()
        re = foo.pre_predict('hamming')
        re.to_csv(output_file_name, sep='\t', index=False)


    input_path = '/home/yangfang/PCSF/no_report/test_re111/input'
    all_input_genes_file = list(filter(lambda f: not f.startswith('.'), os.listdir(input_path)))
    tasks = check_task(all_input_genes_file)
    cores = 6
    pool = multiprocessing.Pool(processes=cores)
    pool.map(run_pre, tasks)

