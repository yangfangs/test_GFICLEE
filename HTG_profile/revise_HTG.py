import pandas as pd
import numpy as np
species = ['Animals','Plants','Fungi','Protists','Prokaryotes']
phylum = {}

#init
for line in species:
    phylum[line] = []
with open("/home/yangfang/GFICLEE/HTG_profile/138_fullnames.csv") as f:
    for line in f:
        tem = line.strip().split(",")
        name = tem[2]
        phy = tem[3].split(";")[1]
        phylum[phy].append(name)

del phylum['Prokaryotes']



df = pd.read_csv("/home/yangfang/GFICLEE/HTG_profile/hsa.matrix138.e3.q00.p20.txt",sep='\t',low_memory=False)
col_name = df.columns.to_numpy()[2:]

def check(profile):
    res = False
    for k, v in phylum.items():
        idx = []
        for lines in v:
            idx.append(np.where(col_name== lines)[0].tolist()[0])
        sub_profile = profile[idx]
        total = len(sub_profile)
        presence = sub_profile.sum()
        if presence <= round(total * 0.15) and presence != 0:
            print(k)
            profile[idx] =0
            print("presence:" + str(presence) + " total:" + str(total) )
            res = True
    return profile,res




id = []
names = []
row_id = []
w_ = open("/home/yangfang/GFICLEE/HTG_profile/hsa.matrix138.e3.q00.p20_revise.txt",'w')
w_.write("\t".join(df.columns.to_list())+"\n")

for data,row in df.iterrows():
    profile = row.to_numpy()[2:]
    profile2,res = check(profile)
    if res:
        row_id.append(data)
        id.append(row[0])
        names.append(row[1])
    if str(row[1]) == 'nan':
        row[1] = ''
    w_.write(str(row[0])+'\t'+row[1] +'\t' + "\t".join(list(map(str,profile2.tolist()))) +"\n")
print(len(id))



