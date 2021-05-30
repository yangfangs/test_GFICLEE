import pandas as pd
import numpy as np

species = ['Animals', 'Plants', 'Fungi', 'Protists', 'Prokaryotes']
phylum = {}

# init
for line in species:
    phylum[line] = []
with open("/home/yangfang/GFICLEE/HTG_profile/138_fullnames.csv") as f:
    for line in f:
        tem = line.strip().split(",")
        name = tem[2]
        phy = tem[3].split(";")[1]
        phylum[phy].append(name)

del phylum['Prokaryotes']

df = pd.read_csv("/home/yangfang/GFICLEE/HTG_profile/hsa.matrix138.e3.q00.p20.txt", sep='\t', low_memory=False)
col_name = df.columns.to_numpy()[2:]


def check(profile):
    for k, v in phylum.items():
        idx = []
        for lines in v:
            idx.append(np.where(col_name == lines)[0].tolist()[0])
        sub_profile = profile[idx]
        total = len(sub_profile)
        presence = sub_profile.sum()
        # if presence <= round(total * 0.1) and presence != 0:
        if presence == 1 and presence != 0:
            print(k)
            print("presence:" + str(presence) + " total:" + str(total))
            return True
    return False


id = []
names = []
row_id = []

for data, row in df.iterrows():
    profile = row.to_numpy()[2:]
    if check(profile):
        row_id.append(data)
        id.append(row[0])
        names.append(row[1])
    break

print(len(id))

df2 = df.drop(row_id)

df2.to_csv("/home/yangfang/GFICLEE/HTG_profile/hsa.matrix138.e3.q00.p20_filter_HTG.txt", sep='\t', index=0)

with open("/home/yangfang/GFICLEE/HTG_profile/entrez_filter_HTG.txt", "w") as f:
    for line in id:
        f.write(str(line) + "\n")

with open("/home/yangfang/GFICLEE/HTG_profile/symbol_filter_HTG.txt", "w") as f:
    for line in names:
        f.write(str(line) + "\n")
