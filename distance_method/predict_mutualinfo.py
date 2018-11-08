import time
from collections import Counter

import numpy as np
from sklearn.metrics import adjusted_mutual_info_score, normalized_mutual_info_score, mutual_info_score

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
                 out_path='/home/yangfang/GFICLEE/distance_method/go/result_mutualinfo',
                 method='mutual_info')
foo.leave_half(input_file_path='/home/yangfang/GFICLEE/distance_method/go/input/',
               leave_file_path='/home/yangfang/GFICLEE/distance_method/go/output/',
               pathway='/home/yangfang/GFICLEE/distance_method/go/human.GO.txt')
foo.run(6)



# get predict for Corum databse


foo = GetPredict(profile_path='/home/yangfang/GFICLEE/distance_method/corum/hsa.matrix138.e3.q00.p20.txt',
                 out_path='/home/yangfang/GFICLEE/distance_method/corum/result_mutualinfo',
                 method='mutual_info')
foo.leave_half(input_file_path='/home/yangfang/GFICLEE/distance_method/corum/input/',
               leave_file_path='/home/yangfang/GFICLEE/distance_method/corum/output/',
               pathway='/home/yangfang/GFICLEE/distance_method/corum/human.corum.txt')
foo.run(6)



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def entropy( labels):
    prob_dict = Counter(labels)
    s = sum(prob_dict.values())
    probs = np.array([i / s for i in prob_dict.values()])
    return -probs.dot(np.log(probs))


def mi_score( a, b):
    a_b = ["{0}{1}".format(i, j) for i, j in zip(a, b)]
    return entropy(a) + entropy(b) - entropy(a_b)


start =time.time()

foo.read_input("/home/yangfang/GFICLEE/distance_method/kegg/input/0_0.txt")
foo.prepare_data()
input_gene = foo.input_genes_data
all_gene_data = foo.profile_data

adjusted_mutual_info_score(input_gene[0],all_gene_data[0])
adjusted_mutual_info_score(input_gene[0],input_gene[0])

all_res = []
for i in input_gene:
    all_pre = []
    for j in all_gene_data:
        all_pre.append(mi_score(i,j))
    all_res.append(all_pre)
all_res_np = np.array(all_res)
all_res_max = all_res_np.max(axis=0)


end = time.time()

print("===============================")
print('Running time: {} Seconds'.format(end-start))


#~~~~~~~~~~~~~~~~~~~~~~
