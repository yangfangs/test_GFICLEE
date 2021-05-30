import time

from GFICLEE.gficlee_predict import GficleePredict

foo = GficleePredict(profile_path='/home/yangfang/GFICLEE/test_kegg_gficlee/hsa.matrix138.e3.q00.p20.txt',
                     tree_path='/home/yangfang/GFICLEE/test_kegg_gficlee/test2_fix.fas_iqtree_rooted.nwk',
                     result_path='/home/yangfang/GFICLEE/test_kegg_gficlee/result/')
# 5-fold cross validation
foo.leave_half('/home/yangfang/GFICLEE/test_kegg_gficlee/input/',
               '/home/yangfang/GFICLEE/test_kegg_gficlee/output/',
               '/home/yangfang/GFICLEE/test_kegg_gficlee/human.KEGG.txt')

start = time.time()
# run test with 6 cores
foo.run_gficlee(6, gficlee_path='/home/yangfang/GFICLEE/GFICLEE1.0.jar')
end = time.time()
print("===============================")
print('Running time: {} Seconds'.format(end - start))
