import os
from os import listdir
from os.path import isfile, join
path=os.path.dirname(os.path.abspath(__file__))
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
onlyfiles.pop()
print(onlyfiles)

for files in onlyfiles:
    f = open(files[:-2] + "_cmd.R", 'w')
    f.write("setwd(\"~/R codes\")\n\n")
    f.write("source(\""+files+"\")\n\n")
    f.write("args <- commandArgs(TRUE)\n\n")
    f.write("result = logic( args[1], args[2] )\n\n")
    f.write("write(result, \""+files[:-2]+"_result.txt\")\n\n")