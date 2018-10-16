from distance_method.get_fpr_tpr_distance import PlotRocHamming


# for Kegg database
foo = PlotRocHamming('/home/yangfang/GFICLEE/distance_method/kegg/input/',
              '/home/yangfang/GFICLEE/distance_method/kegg/output/',
              '/home/yangfang/GFICLEE/distance_method/kegg/human.KEGG.txt',
              '/home/yangfang/GFICLEE/distance_method/kegg/result_euclidean/')
# threshold

thr = [i / 40 for i in range(40)][:34]

all_tpr_fpr_precision, all_r = foo.start_roc(6, thr)

foo.write_tpr_fpr(all_tpr_fpr_precision,
                  '/home/yangfang/GFICLEE/distance_method/kegg/kegg_tpr_fpr_precision_euclidean.txt')
foo.write_all(all_r,
              '/home/yangfang/GFICLEE/distance_method/kegg/kegg_tp_fp_tn_fn_euclidean.txt')
