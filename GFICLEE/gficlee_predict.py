import multiprocessing
import pandas as pd
import os
import subprocess


class GficleePredict(object):
    def __init__(self,profile_path,
                 tree_path,
                 result_path):
        self.input_path = ''
        self.leave_path = ''
        self.profile_path = profile_path
        self.tree_path =tree_path
        self.result_path = result_path
        if not os.path.isdir(result_path):
            os.makedirs(result_path)

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
        self.input_path = input_file_path
        self.leave_path = leave_file_path


    def run_cmd(self,cmd):
        subprocess.call(cmd, shell=True)


    def run_gficlee(self,core,gficlee_path='GFICLEE'):
        all_cmd = []
        path = self.input_path
        all_file = list(filter(lambda f: not f.startswith('.'), os.listdir(path)))
        for line in all_file:
            i_ = os.path.join(path,line)
            t_ = self.tree_path
            p_ = self.profile_path
            o_ = os.path.join(self.result_path,line)
            # if not os.path.isdir(o_):
            #     os.makedirs(o_)
            cmd = "java -jar " + gficlee_path + " -i " + i_ + " -p " + p_ + " -t " + t_ + " -o " + o_
            all_cmd.append(cmd)
        # Do multiple processing
        cores = core
        pool = multiprocessing.Pool(processes=cores)
        # method 1: map
        pool.map(self.run_cmd, all_cmd)
