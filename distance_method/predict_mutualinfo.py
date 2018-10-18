from sklearn.metrics import adjusted_mutual_info_score, normalized_mutual_info_score

from distance_method.distance_predict import GetPredict



# get predict for kegg database
foo = GetPredict(profile_path='/home/yangfang/GFICLEE/distance_method/kegg/hsa.matrix138.e3.q00.p20.txt',
                 out_path='/home/yangfang/GFICLEE/distance_method/kegg/result_mutualinfo',
                 method='mutual_info')
foo.leave_half(input_file_path='/home/yangfang/GFICLEE/distance_method/kegg/input/',
               leave_file_path='/home/yangfang/GFICLEE/distance_method/kegg/output/',
               pathway='/home/yangfang/GFICLEE/distance_method/kegg/human.KEGG.txt')
foo.run(6)


# get predict for Go database
foo = GetPredict(profile_path='/home/yangfang/GFICLEE/distance_method/go/hsa.matrix138.e3.q00.p20.txt',
                 out_path='/home/yangfang/GFICLEE/distance_method/go/result_euclidean',
                 method='mutual_info')
foo.leave_half(input_file_path='/home/yangfang/GFICLEE/distance_method/go/input/',
               leave_file_path='/home/yangfang/GFICLEE/distance_method/go/output/',
               pathway='/home/yangfang/GFICLEE/distance_method/go/human.GO.txt')
foo.run(6)



# get predict for Corum databse


foo = GetPredict(profile_path='/home/yangfang/GFICLEE/distance_method/corum/hsa.matrix138.e3.q00.p20.txt',
                 out_path='/home/yangfang/GFICLEE/distance_method/corum/result_euclidean',
                 method='mutual_info')
foo.leave_half(input_file_path='/home/yangfang/GFICLEE/distance_method/corum/input/',
               leave_file_path='/home/yangfang/GFICLEE/distance_method/corum/output/',
               pathway='/home/yangfang/GFICLEE/distance_method/corum/human.corum.txt')
foo.run(6)


foo.read_input("/home/yangfang/GFICLEE/distance_method/kegg/input/0_0.txt")
foo.prepare_data()
input_gene = foo.input_genes_data
all_gene_data = foo.profile_data

adjusted_mutual_info_score(input_gene[0],all_gene_data[0])
adjusted_mutual_info_score(input_gene[0],input_gene[0])
all_pre = []
all_res = []
for i in all_gene_data[:10]:
    for j in input_gene:
        adjusted_mutual_info_score(j,i)
        all_pre.append(adjusted_mutual_info_score(j,i))
    all_res.append(max(all_pre))
print(all_res)