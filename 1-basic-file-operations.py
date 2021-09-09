import os, sys

# write to a file
myfile1 = open(os.path.join(sys.path[0], "1-data.txt"), 'a')
myfile1.write("Jibreel Islam\n")
myfile1.close()


# read from a file
myfile2 = open(os.path.join(sys.path[0], "1-data.txt"), 'r')
file_content = myfile2.read()
myfile2.close()

print(file_content)

