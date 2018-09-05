# plot clime roc

import pandas as pd
import os
import multiprocessing
import numpy as np

# get tpr and fpr
import sys


class PlotRoc(object):
    def __init__(self,
                 input_gene_path,
                 leave_gene_path,
                 input_all_path,
                 predict_path,
                 ):
        self.input_gene_path = input_gene_path
        self.leave_gene_path = leave_gene_path
        self.input_all_path = input_all_path
        self.predict_path = predict_path

    def get_input_clime_name(self, genes):
        input_pathway = pd.read_csv(genes, sep='\t')
        p_name = list(input_pathway.Symbol)
        return p_name

    def tans_predict(self, pre_path, p_name, n_name):
        # read predict
        data = pd.read_csv(pre_path, sep='\t')
        # get ecm+ and llr
        re = data

        re_symbol = list(re['name'])
        re_llr = list(re['score'])
        # if p_name not in predict result
        not_pre_p_names = [x for x in p_name if x not in re_symbol]
        # n_name not in predict result

        not_pre_n_names = [x for x in n_name if x not in re_symbol]
        if not_pre_p_names:
            re_symbol.extend(not_pre_p_names)
            llr = [float("-inf")] * len(not_pre_p_names)
            re_llr.extend(llr)
        if not_pre_n_names:
            re_symbol.extend(not_pre_n_names)
            llr2 = [float("-inf")] * len(not_pre_n_names)
            re_llr.extend(llr2)
        # change col names
        dic = {'name': re_symbol, 'score': re_llr}
        pre = pd.DataFrame(dic)
        pre = pre.sort_values('score', ascending=False)

        return pre

    def get_tpr_fpr(self, p_name: list,
                    n_name: list,
                    threshold: int,
                    pre: 'dataframe', ) -> "The tpr and fpr":
        """
        Get fpr and tpr
        :param p_name: Positive genes
        :param n_name: Negative genes
        :param threshold: The threshold
        :param pre: The predict dataframe
        :return: tpr and fpr
        """

        # bayes threshold
        threshold_up = list(pre.name[pre.score >= threshold])
        threshold_down = list(pre.name[pre.score < threshold])

        # # distance threshold
        # threshold_up = list(pre.name[pre.score <= threshold])
        # threshold_down = list(pre.name[pre.score > threshold])
        tp = len([x for x in p_name if x in threshold_up])
        fp = len([x for x in n_name if x in threshold_up])
        tn = len([x for x in n_name if x in threshold_down])
        fn = len([x for x in p_name if x in threshold_down])
        # print((tp, fp, tn, fn))

        tpr = tp / (tp + fn)

        fpr = fp / (fp + tn)
        if tp + fp == 0:
            precision = np.nan
        else:
            precision = tp / (tp + fp)

        return precision, tpr, fpr, (tp, fp, tn, fn)  # do every threshold

    # kegg_matrix = pd.read_csv('/home/yangfang/PCSF/clime_roc/all_kegg_matrix.txt', sep='\t')
    #
    # all_genes = list(kegg_matrix.Symbol)




    # get leave genes names
    def get_leave_genes(self, path):
        df = pd.read_csv(path, sep='\t')
        leave_genes = list(df['Symbol'])
        return leave_genes

    def run_roc(self, pred, i):

        input_gene_file_names = pred

        input_gene_abs = self.input_gene_path
        leave_gene_abs = self.leave_gene_path
        input_gene_file = os.path.join(input_gene_abs, input_gene_file_names)
        leave_gene_file = os.path.join(leave_gene_abs, input_gene_file_names)
        # get leave out genes names as positive
        p_names = self.get_leave_genes(leave_gene_file)

        # get negative genes names
        input_clime = self.get_input_clime_name(input_gene_file)

        # append positive genes
        input_clime.extend(p_names)
        input_genes = pd.read_csv(self.input_all_path, sep='\t')

        all_pathway_genes = list(input_genes['Symbol'])
        all_pathway_genes = list(set(all_pathway_genes))

        n_names = [var for var in all_pathway_genes if var not in input_clime]
        pre = self.tans_predict(os.path.join(self.predict_path, pred), p_names, n_names)
        # pre = pd.read_csv(os.path.join('/home/yangfang/PCSF/knn_roc/result_all_n15_remove_input', pred), sep='\t')

        precision, tpr, fpr, all_r = self.get_tpr_fpr(p_names, n_names, i, pre)
        return (precision, tpr, fpr, all_r)

    def get_mean_with_nan(self,arr):
        each_col_mean = []
        arr_col = arr.shape[1]
        for i in range(arr_col):
            tem = arr[:,i]
            tem = tem[-np.isnan(tem)]
            each_col_mean.append(tem.mean())
        return np.array(each_col_mean)

    def run_num(self, num, thre):
        result = []
        all_pre_file_path = self.predict_path
        all_pre_file = list(filter(lambda f: not f.startswith('.'), os.listdir(all_pre_file_path)))
        star = str(num) + '_'
        each_pathway = [x for x in all_pre_file if x.startswith(str(star))]

        for i in each_pathway:
            re = self.run_roc(i, thre)
            result.append(re)

        # get each result
        precision_tpr_fpr = [var[:3] for var in result]
        all_r = [var[-1] for var in result]
        # trans to array
        precision_tpr_fpr_array = np.array(precision_tpr_fpr)

        # remove nan
        mdat = np.ma.masked_array(precision_tpr_fpr_array, np.isnan(precision_tpr_fpr_array))
        mm = np.mean(mdat, axis=0)
        # get each mean
        mean_p_tpr_fpr_array = mm.filled(np.nan)
        # get two pathway mean

        return mean_p_tpr_fpr_array, all_r

    def start_roc(self, core, thr):
        all_r = []
        all_tpr_fpr_precision = []
        all_pre_file_path = self.predict_path
        all_pre_file = list(filter(lambda f: not f.startswith('.'), os.listdir(all_pre_file_path)))
        all_num = [x[:-6] for x in all_pre_file]
        all_num = list(set(all_num))

        for i in thr:
            print(i)
            # # ~~~~~~~~~~~~~~~
            # i=1
            # all_num = range(6)
            # # ~~~~~~~~~~~~~~~~
            each_result = []

            tasks = [(x, y) for x in all_num for y in [i]]
            cores = core
            pool = multiprocessing.Pool(processes=cores)
            # map
            result = pool.starmap(self.run_num, tasks)
            pool.close()
            pool.join()

            each_result_array = np.array([x[0] for x in result])
            each_r = [x for z in result for x in z[1]]

            #re nan
            mdat = np.ma.masked_array(each_result_array, np.isnan(each_result_array))
            mm = np.mean(mdat, axis=0)
            # get each mean
            all_mean_p_t_f_array = mm.filled(np.nan)



            # all_mean_p_t_f_array = each_result_array.mean(axis=0)
            mean_precision = all_mean_p_t_f_array[0]
            mean_tpr = all_mean_p_t_f_array[1]
            mean_fpr = all_mean_p_t_f_array[2]
            print(mean_tpr, mean_fpr, mean_precision)
            all_tpr_fpr_precision.append((mean_tpr, mean_fpr, mean_precision))
            all_r.extend(each_r)

        return all_tpr_fpr_precision, all_r

    def write_tpr_fpr(self, all_tpr_fpr_precision, path):
        f = open(path, 'a')
        f.write('tpr\tfpr\tprecision\n')

        for i in all_tpr_fpr_precision:
            f.write('{0}\t{1}\t{2}\n'.format(i[0], i[1], i[2]))

        f.close()

    def write_all(self, all_r, path):
        f2 = open(path, 'a')
        f2.write('tp\tfp\ttn\tfn\n')

        for j in all_r:
            f2.write('{0}\t{1}\t{2}\t{3}\n'.format(j[0], j[1], j[2], j[3]))
        f2.close()

