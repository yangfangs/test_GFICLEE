
from distance_method.distance_predict import GetPredict



# get predict for kegg database
foo = GetPredict(profile_path='/home/yangfang/GFICLEE/distance_method/kegg/hsa.matrix138.e3.q00.p20.txt',
                 out_path='/home/yangfang/GFICLEE/distance_method/kegg/result_hamming',
                 method='hamming')
foo.leave_half(input_file_path='/home/yangfang/GFICLEE/distance_method/kegg/input/',
               leave_file_path='/home/yangfang/GFICLEE/distance_method/kegg/output/',
               pathway='/home/yangfang/GFICLEE/distance_method/kegg/human.KEGG.txt')
foo.run(6)


# get predict for Go database
foo = GetPredict(profile_path='/home/yangfang/GFICLEE/distance_method/go/hsa.matrix138.e3.q00.p20.txt',
                 out_path='/home/yangfang/GFICLEE/distance_method/go/result_hamming',
                 method='hamming')
foo.leave_half(input_file_path='/home/yangfang/GFICLEE/distance_method/go/input/',
               leave_file_path='/home/yangfang/GFICLEE/distance_method/go/output/',
               pathway='/home/yangfang/GFICLEE/distance_method/go/human.GO.txt')
foo.run(6)



# get predict for Corum databse


foo = GetPredict(profile_path='/home/yangfang/GFICLEE/distance_method/corum/hsa.matrix138.e3.q00.p20.txt',
                 out_path='/home/yangfang/GFICLEE/distance_method/corum/result_hamming',
                 method='hamming')
foo.leave_half(input_file_path='/home/yangfang/GFICLEE/distance_method/corum/input/',
               leave_file_path='/home/yangfang/GFICLEE/distance_method/corum/output/',
               pathway='/home/yangfang/GFICLEE/distance_method/corum/human.corum.txt')
foo.run(6)