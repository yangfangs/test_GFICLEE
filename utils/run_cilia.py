import os
import subprocess

path = '/home/yangfang/GFICLEE/cilia/input/'
result_path = "/home/yangfang/GFICLEE/cilia/result/"

files = list(filter(lambda f: not f.startswith('.'), os.listdir(path)))
gficlee_path = '/home/yangfang/GFICLEE/GFICLEE1.0.jar'
for line in files:
    i_ = os.path.join(path, line)
    t_ = "/home/yangfang/GFICLEE/cilia/species138.abbrev.manual_binary.nwk"
    p_ = "/home/yangfang/GFICLEE/cilia/hsa.matrix138.e3.q00.p20.txt"
    o_ = os.path.join(result_path, line)
    # if not os.path.isdir(o_):
    #     os.makedirs(o_)
    cmd = "java -jar " + gficlee_path + " -i " + i_ + " -p " + p_ + " -t " + t_ + " -o " + o_
    subprocess.call(cmd, shell=True)