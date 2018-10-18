# parser ath
import re


write_file = open("/home/yangfang/GFICLEE/test_ath_gficlee/ath00001_trans.txt",'w')


pathway =["Metabolism","Cellular Processes","Genetic Information Processing"]


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
