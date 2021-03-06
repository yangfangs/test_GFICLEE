import os
import pandas as pd

from ROC.get_fpr_tpr import PlotRoc

#First transform clime result for calculate tpr and fpr
def trans_clime(input_path, out_path,name):
    if not os.path.isdir(out_path):
        os.makedirs(out_path)
    all_pre_file = list(filter(lambda f: not f.startswith('.'), os.listdir(input_path)))
    for i in all_pre_file:
        read_file = os.path.join(input_path, i)
        w_name = i[:-6]
        w_path_name = os.path.join(out_path, w_name)
        # read predict
        data = pd.read_csv(read_file, sep='\t')
        # get ecm+ and llr
        re = data[[name, 'LLR']][data['ECM/ECM+'].isin(['ECM+'])]
        names = ['name', 'score']
        re.columns = names
        re = re.sort_values('score', ascending=False)
        re.to_csv(w_path_name, sep='\t', index=False)

trans_clime('/home/yangfang/GFICLEE/test_ath_clime/result_all5/',
            '/home/yangfang/GFICLEE/test_ath_clime/result_all_trans5/',
            'Gene Symbol')

#Second get fpr and tpr




foo = PlotRoc('/home/yangfang/GFICLEE/test_ath_clime/input/',
              '/home/yangfang/GFICLEE/test_ath_clime/output/',
              '/home/yangfang/GFICLEE/test_ath_clime/ath00001_5_filter.txt',
              '/home/yangfang/GFICLEE/test_ath_clime/result_all_trans5/')
# threshold
thr = list(reversed([i / 2.0 for i in range(120)]))


# thr = list(reversed([i / 1 for i in range(0, 20)]))
# thr2 = [-x / 1 for x in list(range(0, 10))]
# thr.extend(thr2)

# thr = list(reversed([i/1  for i in range(0, 25)]))
# thr2 = [-x / 2 for x in list(range(0, 20,1))]
# thr.extend(thr2)
# thr = [-x / 1 for x in list(range(50, 130,2))][-25:]
# thr = list([i / 500 for i in range(60)])[0:30]
all_tpr_fpr_precision, all_r = foo.start_roc(6, thr)

foo.write_tpr_fpr(all_tpr_fpr_precision,
                  '/home/yangfang/GFICLEE/test_ath_clime/ath_tpr_fpr_precision_clime5.txt')
foo.write_all(all_r,
              '/home/yangfang/GFICLEE/test_ath_clime/ath_tp_fp_tn_fn_clime5.txt')
