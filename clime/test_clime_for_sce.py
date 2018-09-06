import time

from clime.clime_predict import ClimePredict

foo = ClimePredict()
# 2-fold cross validation
foo.leave_half('/home/yangfang/GFICLEE/test_sce/input/', '/home/yangfang/GFICLEE/test_sce/output/',
               '/home/yangfang/GFICLEE/test_sce/sce.genome.txt')
# generate the clime parameters for test
foo.get_prm('/home/yangfang/GFICLEE/test_sce/template.prms',
            '//home/yangfang/GFICLEE/test_sce/prms_all/',
            '/home/yangfang/GFICLEE/test_sce/result_all/')

start =time.time()
# run test with 6 cores
foo.run_clime(6, clime_path='/home/yangfang/tools/clime')
end = time.time()
print("===============================")
print('Running time: {} Seconds'.format(end-start))