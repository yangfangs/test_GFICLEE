import multiprocessing
import pandas as pd
import os
import subprocess


class ClimePredict(object):
    def __init__(self):
        self.input_path = ''
        self.leave_path = ''
        self.prms_path = ''
        self.result_path = ''

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
            for j in range(5):
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
        self.input_path = input_file_path
        self.leave_path = leave_file_path

    def get_prm(self, template_path, prms_out_path, result_out_file):

        if not os.path.isdir(result_out_file):
            os.makedirs(result_out_file)
        if not os.path.isdir(prms_out_path):
            os.makedirs(prms_out_path)

        template = pd.read_csv(template_path, sep='\t')
        path = self.input_path
        all_file = list(filter(lambda f: not f.startswith('.'), os.listdir(path)))

        for j in all_file:
            input_gene_path = os.path.join(path, j)
            out_path = os.path.join(result_out_file, j)
            write_path = os.path.join(prms_out_path, j.replace('.txt', '.prms'))
            template.iloc[2, 0] = input_gene_path

            template.iloc[3, 0] = out_path
            template.to_csv(write_path, sep='\t')
        self.prms_path = prms_out_path
        self.result_path = result_out_file


    def run_cmd(self,cmd):
        subprocess.call(cmd, shell=True)


    def run_clime(self,core,clime_path='clime'):
        prims_path = self.prms_path
        all_prims_file = list(filter(lambda f: not f.startswith('.'), os.listdir(prims_path)))
        all_cmd = []

        for i in all_prims_file:
            prims_abs = os.path.join(prims_path, i)
            cmd = clime_path + ' ' + prims_abs + ' 0'
            all_cmd.append(cmd)
        # Do multiple processing
        cores = core
        pool = multiprocessing.Pool(processes=cores)
        # method 1: map
        pool.map(self.run_cmd, all_cmd)



if __name__ == '__main__':
    foo = ClimePredict()
    foo.leave_half('/home/yangfang/PCSF/input/', '/home/yangfang/PCSF/output',
                   '/home/yangfang/PCSF/clime_roc/human.KEGG.txt')
    foo.get_prm('/home/yangfang/PCSF/clime_roc/human_CI_half.prms',
                '/home/yangfang/PCSF/test_re112/prms_all/',
                '/home/yangfang/PCSF/test_re112/result_all/')
    # foo.run_clime(6)