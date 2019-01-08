from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir("/Users/mashrafihaider/PycharmProjects/Maths") if isfile(join("/Users/mashrafihaider/PycharmProjects/Maths", f))]

print(onlyfiles)

for files in onlyfiles:
    with open(files) as myfile:
        head = [next(myfile) for x in xrange(3)]

    function = head[0][1:].rstrip()
    parameter = head[1][1:].rsplit()
    re = head[2][1:].rstrip()
    f=open(files[:-3]+"Wrapped.py",'w')
    f.write("from ProvModel import Object, File, Document, Module\n")
    f.write("from ProvModel import err\n")
    f.write("from Operators import jsonify\n")
    f.write("import "+files+'\n')
    f.write("class "+function+"(Module):"+"\n")
    f.write("\t"+"def body(self):"+'\n')
    str1=''
    for i in range(len(parameter)-1):

        f.write('\t'+'\t'+str(parameter[i])+" = self.P["+str(i)+"].ref\n")
        str1=str1+str(parameter[i])+','
    str1=str1+str(parameter[-1])
    f.write('\t\t'+re+" = "+function+'.'+function+'('+str1+')\n')
    f.write('\t\t'+'return '+'Object('+re+')')


    # f=open(files,"r")
    # for line in f:
    #     print(line)

