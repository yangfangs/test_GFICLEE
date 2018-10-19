from distance_method.get_fpr_tpr_distance import PlotRocDistance



# get fpr tpr for kegg database
foo = PlotRocDistance('/home/yangfang/GFICLEE/distance_method/kegg/input/',
              '/home/yangfang/GFICLEE/distance_method/kegg/output/',
              '/home/yangfang/GFICLEE/distance_method/kegg/human.KEGG.txt',
              '/home/yangfang/GFICLEE/distance_method/kegg/result_jaccard/')
# threshold

thr = [i / 60 for i in range(40)]

all_tpr_fpr_precision, all_r = foo.start_roc(6, thr)

foo.write_tpr_fpr(all_tpr_fpr_precision,
                  '/home/yangfang/GFICLEE/distance_method/kegg/kegg_tpr_fpr_precision_jaccard.txt')
foo.write_all(all_r,
              '/home/yangfang/GFICLEE/distance_method/kegg/kegg_tp_fp_tn_fn_jaccard.txt')


# get fpr tpr for GO database
foo = PlotRocDistance('/home/yangfang/GFICLEE/distance_method/go/input/',
              '/home/yangfang/GFICLEE/distance_method/go/output/',
              '/home/yangfang/GFICLEE/distance_method/go/human.GO.txt',
              '/home/yangfang/GFICLEE/distance_method/go/result_jaccard/')
# threshold

thr = [i / 60 for i in range(40)]

all_tpr_fpr_precision, all_r = foo.start_roc(6, thr)

foo.write_tpr_fpr(all_tpr_fpr_precision,
                  '/home/yangfang/GFICLEE/distance_method/go/go_tpr_fpr_precision_jaccard.txt')
foo.write_all(all_r,
              '/home/yangfang/GFICLEE/distance_method/go/go_tp_fp_tn_fn_jaccard.txt')