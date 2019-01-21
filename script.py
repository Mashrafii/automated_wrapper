import os
import ProvModel as pm
import sys
import subprocess

class Script(pm.Module):

    def body(self):
        #The first input from the command line which should be the language we are using
        lang=self.P[0]
        #The second input from the command line in which we should have the file which we want to run
        path=self.P[1]
        #The third input from the command line in which we should have the output file path
        output=self.P[2]
        outputString=output.ref
        langString=lang.ref
        pathString=path.ref
        if(langString=="java"):
            cmd="javac "+pathString
            #command to compile the file
            os.system(cmd)
            cmd1="java "+pathString
            #command to run the file
            os.system(cmd1)
        elif(langString=="R"):
            #command to run the file
            cmd="RScript "+pathString
            os.system(cmd)


        #open the file where the output is stored
        p=open(outputString)
        #pack it to the object
        res=pm.File(p)

        return res
list=sys.argv
#first input which is the language
lang=list[1]
# second input which is the file that we will run
path=list[2]
#the third input in the console which is the output file
output=list[3]
inputLang=pm.Object(lang)
inputPath=pm.Object(path)
outputPath=pm.Object(output)

class1=Script(inputLang,inputPath,outputPath)
class2=class1.run()





# module_1_input="/Users/mashrafihaider/PycharmProjects/Spark/wordcount.py"
#
# input=pm.Object(module_1_input)
#
# input1=Spark(input)
#
# inp=input1.run()

