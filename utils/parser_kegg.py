# parser ath
import re


write_file = open("/home/yangfang/GFICLEE/test_ath_gficlee/ath00001_5.txt",'w')


pathway =["Metabolism","Cellular Processes","Genetic Information Processing","Environmental Information Processing","Organismal Systems"]

# pathway =["Metabolism","Cellular Processes"]
with open('/home/yangfang/GFICLEE/test_ath_gficlee/ath00001.keg') as f:
    for line in f:
        if line.startswith("A"):
            A_ = line.strip()[7:]
            if A_ in pathway:
                print(A_)
        if line.startswith("B") and line.strip() != "B":
            B_ = line.strip()[9:]
        if line.startswith("C"):
            C_ = line.strip()
            if C_[-1] == "]":
                C_ = C_[11:-16]
            else:
                C_ = C_[11:]
        if line.startswith("D"):
            regex = re.compile('\s+')
            D_ = line.strip().split(";")
            D_entrez = regex.split(D_[0])[1]
            if A_ in pathway:
                write_file.write("{0}\t{1}\n".format(D_entrez,C_))



# parser cme
import re


write_file = open("/home/yangfang/GFICLEE/test_cme_gficlee/cme.genome2.txt",'w')


pathway =["Metabolism","Cellular Processes","Genetic Information Processing","Environmental Information Processing","Organismal Systems"]

# pathway =["Metabolism","Cellular Processes"]
with open('/home/yangfang/GFICLEE/test_cme_gficlee/cme00001.keg') as f:
    for line in f:
        if line.startswith("A"):
            A_ = line.strip()[7:]
            if A_ in pathway:
                print(A_)
        if line.startswith("B") and line.strip() != "B":
            B_ = line.strip()[9:]
        if line.startswith("C"):
            C_ = line.strip()
            if C_[-1] == "]":
                C_ = C_[11:-16]
            else:
                C_ = C_[11:]
        if line.startswith("D"):
            regex = re.compile('\s+')
            D_ = line.strip().split(";")
            D_entrez = regex.split(D_[0])[1][5:]
            if A_ in pathway:
                write_file.write("{0}\t{1}\n".format(D_entrez,C_))

# parser cel
import re


write_file = open("/home/yangfang/GFICLEE/test_cel_gficlee/cel.genome.txt",'w')


pathway =["Metabolism","Cellular Processes","Genetic Information Processing","Environmental Information Processing","Organismal Systems"]

# pathway =["Metabolism","Cellular Processes"]
with open('/home/yangfang/GFICLEE/test_cel_gficlee/cel00001.keg') as f:
    for line in f:
        if line.startswith("A"):
            A_ = line.strip()[7:]
            if A_ in pathway:
                print(A_)
        if line.startswith("B") and line.strip() != "B":
            B_ = line.strip()[9:]
        if line.startswith("C"):
            C_ = line.strip()
            if C_[-1] == "]":
                C_ = C_[11:-16]
            else:
                C_ = C_[11:]
        if line.startswith("D"):
            regex = re.compile('\s+')
            D_ = line.strip().split(";")
            D_entrez = regex.split(D_[0])[1]
            if D_entrez.startswith("CELE_"):
                D_entrez = D_entrez[5:]
            else:
                D_entrez = D_entrez

            if A_ in pathway:
                write_file.write("{0}\t{1}\n".format(D_entrez,C_))
#mmu
import re


write_file = open("/home/yangfang/GFICLEE/test_mmu_gficlee/mmu.genome.txt",'w')


pathway =["Metabolism","Cellular Processes","Genetic Information Processing","Environmental Information Processing","Organismal Systems"]

# pathway =["Metabolism","Cellular Processes"]
with open('/home/yangfang/GFICLEE/test_mmu_gficlee/mmu00001.keg') as f:
    for line in f:
        if line.startswith("A"):
            A_ = line.strip()[7:]
            if A_ in pathway:
                print(A_)
        if line.startswith("B") and line.strip() != "B":
            B_ = line.strip()[9:]
        if line.startswith("C"):
            C_ = line.strip()
            if C_[-1] == "]":
                C_ = C_[11:-16]
            else:
                C_ = C_[11:]
        if line.startswith("D"):
            regex = re.compile('\s+')
            D_ = line.strip().split(";")
            D_entrez = regex.split(D_[0])[2]
            if A_ in pathway:
                write_file.write("{0}\t{1}\n".format(D_entrez,C_))

# parser ncr
import re


write_file = open("/home/yangfang/GFICLEE/test_ncr_gficlee/ncr00001.txt",'w')


pathway =["Metabolism","Cellular Processes","Genetic Information Processing","Environmental Information Processing","Organismal Systems"]

# pathway =["Metabolism","Cellular Processes"]
with open('/home/yangfang/GFICLEE/test_ncr_gficlee/ncr00001.keg') as f:
    for line in f:
        if line.startswith("A"):
            A_ = line.strip()[7:]
            if A_ in pathway:
                print(A_)
        if line.startswith("B") and line.strip() != "B":
            B_ = line.strip()[9:]
        if line.startswith("C"):
            C_ = line.strip()
            if C_[-1] == "]":
                C_ = C_[11:-16]
            else:
                C_ = C_[11:]
        if line.startswith("D"):
            regex = re.compile('\s+')
            D_ = line.strip().split(";")
            D_entrez = regex.split(D_[0])[1]
            if A_ in pathway:
                write_file.write("{0}\t{1}\n".format(D_entrez,C_))


# parser tbr
import re


write_file = open("/home/yangfang/GFICLEE/test_tbr_gficlee/tbr.genome_org.txt",'w')


pathway =["Metabolism","Cellular Processes","Genetic Information Processing","Environmental Information Processing","Organismal Systems"]

# pathway =["Metabolism","Cellular Processes"]
with open('/home/yangfang/GFICLEE/test_tbr_gficlee/tbr00001.keg') as f:
    for line in f:
        if line.startswith("A"):
            A_ = line.strip()[7:]
            if A_ in pathway:
                print(A_)
        if line.startswith("B") and line.strip() != "B":
            B_ = line.strip()[9:]
        if line.startswith("C"):
            C_ = line.strip()
            if C_[-1] == "]":
                C_ = C_[11:-16]
            else:
                C_ = C_[11:]
        if line.startswith("D"):
            regex = re.compile('\s+')
            D_ = line.strip().split(";")
            D_entrez = regex.split(D_[0])[1]
            if A_ in pathway:
                write_file.write("{0}\t{1}\n".format(D_entrez,C_))

# hsa
import re


write_file = open("/home/yangfang/GFICLEE/hsa_kegg/hsa_kegg.txt",'w')


# pathway =["Metabolism","Cellular Processes","Genetic Information Processing","Environmental Information Processing","Organismal Systems"]
pathway =["Metabolism","Cellular Processes","Genetic Information Processing","Environmental Information Processing",]

# pathway =["Metabolism","Cellular Processes"]
with open('/home/yangfang/GFICLEE/hsa_kegg/hsa00001.keg') as f:
    for line in f:
        if line.startswith("A"):
            A_ = line.strip()[7:]
            if A_ in pathway:
                print(A_)
        if line.startswith("B") and line.strip() != "B":
            B_ = line.strip()[9:]
        if line.startswith("C"):
            C_ = line.strip()
            if C_[-1] == "]":
                C_ = C_[11:-16]
            else:
                C_ = C_[11:]
        if line.startswith("D"):
            regex = re.compile('\s+')
            D_ = line.strip().split(";")
            D_entrez = regex.split(D_[0])[2]
            if A_ in pathway:
                write_file.write("{0}\t{1}\n".format(D_entrez,C_))