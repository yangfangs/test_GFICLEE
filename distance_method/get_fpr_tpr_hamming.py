from distance_method.get_fpr_tpr_distance import PlotRocHamming

foo = PlotRocHamming('/home/yangfang/GFICLEE/distance_method/kegg/input/',
              '/home/yangfang/GFICLEE/distance_method/kegg/output/',
              '/home/yangfang/GFICLEE/distance_method/kegg/human.KEGG.txt',
              '/home/yangfang/GFICLEE/distance_method/kegg/result/')
# threshold

thr = [i / 60 for i in range(40)]

all_tpr_fpr_precision, all_r = foo.start_roc(6, thr)

foo.write_tpr_fpr(all_tpr_fpr_precision,
                  '/home/yangfang/GFICLEE/distance_method/kegg/kegg_tpr_fpr_precision_hamming.txt')
foo.write_all(all_r,
              '/home/yangfang/GFICLEE/distance_method/kegg/kegg_tp_fp_tn_fn_hamming.txt')
