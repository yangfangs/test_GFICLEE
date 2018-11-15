import time

from clime.clime_predict import ClimePredict

foo = ClimePredict()
# 2-fold cross validation
foo.leave_half('/home/yangfang/GFICLEE/test_cel_clime/input/', '/home/yangfang/GFICLEE/test_cel_clime/output/',
               '/home/yangfang/GFICLEE/test_cel_clime/cel.genome_filter.txt')
# generate the clime parameters for test
foo.get_prm('/home/yangfang/GFICLEE/test_cel_clime/template.prms',
            '//home/yangfang/GFICLEE/test_cel_clime/prms_all/',
            '/home/yangfang/GFICLEE/test_cel_clime/result_all/')

start =time.time()
# run test with 6 cores
foo.run_clime(6, clime_path='/home/yangfang/tools/clime')
end = time.time()
print("===============================")
print('Running time: {} Seconds'.format(end-start))