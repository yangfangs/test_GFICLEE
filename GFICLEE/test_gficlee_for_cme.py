import time

from GFICLEE.gficlee_predict import GficleePredict

foo = GficleePredict(profile_path='/home/yangfang/GFICLEE/test_cme_gficlee/cme.matrix138.e3.q00.p20.txt',
                     tree_path='/home/yangfang/GFICLEE/test_cme_gficlee/species138.abbrev.manual_binary.nwk',
                     result_path='/home/yangfang/GFICLEE/test_cme_gficlee/result/')
# 2-fold cross validation
foo.leave_half('/home/yangfang/GFICLEE/test_cme_gficlee/input/',
               '/home/yangfang/GFICLEE/test_cme_gficlee/output/',
               '/home/yangfang/GFICLEE/test_cme_gficlee/cme.genome.txt')


start =time.time()
# run test with 6 cores
foo.run_gficlee(6, gficlee_path='GFICLEE')
end = time.time()
print("===============================")
print('Running time: {} Seconds'.format(end-start))