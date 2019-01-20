# <this script name>
# x, y
# sum

logic <- function(x, y)
{
  # the function will always take string inputs because they are coming from command line as string arguments
  # change the type of input parameters that is the responsibility of the raw function
  as.integer(x) + as.integer(y)
}


# the first 3 lines are the configurations
# frst one gives the auto generated class name for ProvMod
# second line contains the name of ordered parameters
# last line contains the name of the result of the function

# the function name can be kept static that is 'logic'
