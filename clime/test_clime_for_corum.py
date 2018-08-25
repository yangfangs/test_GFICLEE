import time

from clime.clime_predict import ClimePredict

foo = ClimePredict()
# 2-fold cross validation
foo.leave_half('/home/yangfang/GFICLEE/test_corum/input/', '/home/yangfang/GFICLEE/test_corum/output/',
               '/home/yangfang/GFICLEE/test_corum/human.KEGG.txt')
# generate the clime parameters for test
foo.get_prm('/home/yangfang/GFICLEE/test_corum/human_CI_half.prms',
            '//home/yangfang/GFICLEE/test_corum/prms_all/',
            '/home/yangfang/GFICLEE/test_corum/result_all/')
start =time.time()
# run test with 6 cores
# foo.run_clime(6)
end = time.time()
print("===============================")
print('Running time: {} Seconds'.format(end-start))