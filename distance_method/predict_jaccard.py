
from distance_method.distance_predict import GetPredict



# get predict for kegg database
foo = GetPredict(profile_path='/home/yangfang/GFICLEE/distance_method/kegg/hsa.matrix138.e3.q00.p20.txt',
                 out_path='/home/yangfang/GFICLEE/distance_method/kegg/result_jaccard',
                 method='jaccard')
foo.leave_half(input_file_path='/home/yangfang/GFICLEE/distance_method/kegg/input/',
               leave_file_path='/home/yangfang/GFICLEE/distance_method/kegg/output/',
               pathway='/home/yangfang/GFICLEE/distance_method/kegg/human.KEGG.txt')
foo.run(6)


# get predict for Go database
foo = GetPredict(profile_path='/home/yangfang/GFICLEE/distance_method/go/hsa.matrix138.e3.q00.p20.txt',
                 out_path='/home/yangfang/GFICLEE/distance_method/go/result_jaccard',
                 method='jaccard')
foo.leave_half(input_file_path='/home/yangfang/GFICLEE/distance_method/go/input/',
               leave_file_path='/home/yangfang/GFICLEE/distance_method/go/output/',
               pathway='/home/yangfang/GFICLEE/distance_method/go/human.GO.txt')
foo.run(6)



# get predict for Corum databse


foo = GetPredict(profile_path='/home/yangfang/GFICLEE/distance_method/corum/hsa.matrix138.e3.q00.p20.txt',
                 out_path='/home/yangfang/GFICLEE/distance_method/corum/result_jaccard',
                 method='jaccard')
foo.leave_half(input_file_path='/home/yangfang/GFICLEE/distance_method/corum/input/',
               leave_file_path='/home/yangfang/GFICLEE/distance_method/corum/output/',
               pathway='/home/yangfang/GFICLEE/distance_method/corum/human.corum.txt')
foo.run(6)


# get predict for ath kegg


foo = GetPredict(profile_path='/home/yangfang/GFICLEE/distance_method/ath/ath_138_matrix.txt',
                 out_path='/home/yangfang/GFICLEE/distance_method/ath/result_jaccard',
                 method='jaccard')
foo.leave_half(input_file_path='/home/yangfang/GFICLEE/distance_method/ath/input/',
               leave_file_path='/home/yangfang/GFICLEE/distance_method/ath/output/',
               pathway='/home/yangfang/GFICLEE/distance_method/ath/ath.KEGG.txt')
foo.run(6)

# get predict for ath kegg


foo = GetPredict(profile_path='/home/yangfang/GFICLEE/distance_method/tbr/tbr.matrix138.e3.q00.p20.txt',
                 out_path='/home/yangfang/GFICLEE/distance_method/tbr/result_jaccard',
                 method='jaccard')
foo.leave_half(input_file_path='/home/yangfang/GFICLEE/distance_method/tbr/input/',
               leave_file_path='/home/yangfang/GFICLEE/distance_method/tbr/output/',
               pathway='/home/yangfang/GFICLEE/distance_method/tbr/tbr.genome.txt')
foo.run(6)