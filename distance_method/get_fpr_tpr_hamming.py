from distance_method.get_fpr_tpr_distance import PlotRocDistance


# for KEGG
foo = PlotRocDistance('/home/yangfang/GFICLEE/distance_method/kegg/input/',
              '/home/yangfang/GFICLEE/distance_method/kegg/output/',
              '/home/yangfang/GFICLEE/distance_method/kegg/human.KEGG.txt',
              '/home/yangfang/GFICLEE/distance_method/kegg/result_hamming/')
# threshold

thr = [i / 60 for i in range(40)]
# thr = [i / 1000 for i in range(10)]

all_tpr_fpr_precision, all_r = foo.start_roc(6, thr)

foo.write_tpr_fpr(all_tpr_fpr_precision,
                  '/home/yangfang/GFICLEE/distance_method/kegg/kegg_tpr_fpr_precision_hamming10.txt')
foo.write_all(all_r,
              '/home/yangfang/GFICLEE/distance_method/kegg/kegg_tp_fp_tn_fn_hamming10.txt')


# for GO

foo = PlotRocDistance('/home/yangfang/GFICLEE/distance_method/go/input/',
              '/home/yangfang/GFICLEE/distance_method/go/output/',
              '/home/yangfang/GFICLEE/distance_method/go/human.GO.txt',
              '/home/yangfang/GFICLEE/distance_method/go/result_hamming/')
# threshold

thr = [i / 60 for i in range(40)]

all_tpr_fpr_precision, all_r = foo.start_roc(6, thr)

foo.write_tpr_fpr(all_tpr_fpr_precision,
                  '/home/yangfang/GFICLEE/distance_method/go/go_tpr_fpr_precision_hamming.txt')
foo.write_all(all_r,
              '/home/yangfang/GFICLEE/distance_method/go/go_tp_fp_tn_fn_hamming.txt')



# for corum
foo = PlotRocDistance('/home/yangfang/GFICLEE/distance_method/corum/input/',
              '/home/yangfang/GFICLEE/distance_method/corum/output/',
              '/home/yangfang/GFICLEE/distance_method/corum/human.corum.txt',
              '/home/yangfang/GFICLEE/distance_method/corum/result_hamming/')
# threshold

thr = [i / 60 for i in range(40)]

all_tpr_fpr_precision, all_r = foo.start_roc(6, thr)

foo.write_tpr_fpr(all_tpr_fpr_precision,
                  '/home/yangfang/GFICLEE/distance_method/corum/corum_tpr_fpr_precision_hamming.txt')
foo.write_all(all_r,
              '/home/yangfang/GFICLEE/distance_method/corum/corum_tp_fp_tn_fn_hamming.txt')



# for ath
foo = PlotRocDistance('/home/yangfang/GFICLEE/distance_method/ath/input/',
              '/home/yangfang/GFICLEE/distance_method/ath/output/',
              '/home/yangfang/GFICLEE/distance_method/ath/ath.KEGG.txt',
              '/home/yangfang/GFICLEE/distance_method/ath/result_hamming/')
# threshold

thr = [i / 60 for i in range(40)]

all_tpr_fpr_precision, all_r = foo.start_roc(6, thr)

foo.write_tpr_fpr(all_tpr_fpr_precision,
                  '/home/yangfang/GFICLEE/distance_method/ath/ath_tpr_fpr_precision_hamming.txt')
foo.write_all(all_r,
              '/home/yangfang/GFICLEE/distance_method/ath/ath_tp_fp_tn_fn_hamming.txt')




# for tbr
foo = PlotRocDistance('/home/yangfang/GFICLEE/distance_method/tbr/input/',
              '/home/yangfang/GFICLEE/distance_method/tbr/output/',
              '/home/yangfang/GFICLEE/distance_method/tbr/tbr.genome.txt',
              '/home/yangfang/GFICLEE/distance_method/tbr/result_hamming/')
# threshold

thr = [i / 60 for i in range(40)]

all_tpr_fpr_precision, all_r = foo.start_roc(6, thr)

foo.write_tpr_fpr(all_tpr_fpr_precision,
                  '/home/yangfang/GFICLEE/distance_method/tbr/tbr_tpr_fpr_precision_hamming.txt')
foo.write_all(all_r,
              '/home/yangfang/GFICLEE/distance_method/tbr/tbr_tp_fp_tn_fn_hamming.txt')
