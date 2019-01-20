# setting working directory to "home/<user name>/R codes"
setwd("~/R codes")

# import target R function from raw source
source("PM_Add.R")

# enable current script to input command line arguments
args <- commandArgs(TRUE)

# pass the arguments into the raw logic function
result = logic( args[1], args[2] )

# save result to disk, you have to create a text file name like <class name from configuration>_result.txt
write(result, "PM_Add_result.txt")


# the command below will generate a result file using the function and the arguments
# Rscript add_cmd 222 333

# this script will be auto generated with the name, '<class name>_cmd.R'