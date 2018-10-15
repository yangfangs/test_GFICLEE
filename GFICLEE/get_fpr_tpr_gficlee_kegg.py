import os
import pandas as pd

from ROC.get_fpr_tpr import PlotRoc

#First transform gficlee result for calculate tpr and fpr
# def trans_gficlee(input_path, out_path):
#     if not os.path.isdir(out_path):
#         os.makedirs(out_path)
#     all_pre_file = list(filter(lambda f: not f.startswith('.'), os.listdir(input_path)))
#     for i in all_pre_file:
#         w_path_name = os.path.join(out_path,i)
#         df = pd.DataFrame(columns=['name', 'score'])
#         all_res = list(filter(lambda f: not f.startswith('.'), os.listdir(os.path.join(input_path,i))))
#         if all_res != []:
#             for j in all_res:
#                 read_path = os.path.join(input_path,i + '/' + j)
#                 data = pd.read_csv(read_path,sep='\t')
#                 df = df.append(data,ignore_index=True)
#         df = df.sort_values('score', ascending=False)
#         df.to_csv(w_path_name,sep='\t',index=False)
#
# trans_gficlee(input_path='/home/yangfang/GFICLEE/test_kegg_gficlee/result/',
#             out_path='/home/yangfang/GFICLEE/test_kegg_gficlee/result_trans/',)

#Second get fpr and tpr




foo = PlotRoc('/home/yangfang/GFICLEE/test_kegg_gficlee/input/',
              '/home/yangfang/GFICLEE/test_kegg_gficlee/output/',
              '/home/yangfang/GFICLEE/test_kegg_gficlee/human.KEGG.txt',
              '/home/yangfang/GFICLEE/test_kegg_gficlee/result/')
# threshold

thr = list(reversed([i/1  for i in range(0, 35)]))
thr2 = [-x / 1 for x in list(range(0, 30,1))]
thr.extend(thr2)

all_tpr_fpr_precision, all_r = foo.start_roc(6, thr)

foo.write_tpr_fpr(all_tpr_fpr_precision,
                  '/home/yangfang/GFICLEE/test_kegg_gficlee/kegg_tpr_fpr_precision_gficlee.txt')
foo.write_all(all_r,
              '/home/yangfang/GFICLEE/test_kegg_gficlee/kegg_tp_fp_tn_fn_gficlee.txt')
