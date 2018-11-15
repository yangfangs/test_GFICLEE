import os
import pandas as pd

from ROC.get_fpr_tpr import PlotRoc




foo = PlotRoc('/home/yangfang/GFICLEE/test_sce_gficlee/input/',
              '/home/yangfang/GFICLEE/test_sce_gficlee/output/',
              '/home/yangfang/GFICLEE/test_sce_gficlee/sce.genome.txt',
              '/home/yangfang/GFICLEE/test_sce_gficlee/result/')
# threshold

thr = list(reversed([i/1  for i in range(0, 20)]))
thr2 = [-x / 1 for x in list(range(0,10,1))]
thr.extend(thr2)

all_tpr_fpr_precision, all_r = foo.start_roc(6, thr)

foo.write_tpr_fpr(all_tpr_fpr_precision,
                  '/home/yangfang/GFICLEE/test_sce_gficlee/sce_tpr_fpr_precision_gficlee.txt')
foo.write_all(all_r,
              '/home/yangfang/GFICLEE/test_sce_gficlee/sce_tp_fp_tn_fn_gficlee.txt')
