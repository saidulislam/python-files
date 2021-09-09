# always having to close the file after we're done working with it is a little tedious.
# Because this is something we have to do every single time we open a file, 
# Python gives us a handy tool called a context manager, which handles these repetitive actions for us.

import os, sys

# read file
with open(os.path.join(sys.path[0], "2-example.txt"), 'r') as example_file:
    print(example_file.read())


# the above code is same as the following

# example_file = open(os.path.join(sys.path[0], "2-example.txt"), "r")
# print(example_file.read())
# example_file.close()

# write to file
with open(os.path.join(sys.path[0], "2-write-file.txt"), 'w') as write_file:
    write_file.write("This is an example file with write functionality in Python")

# appending to file
with open(os.path.join(sys.path[0], "2-append-file.txt"), "a") as append_file:
    append_file.write("\nanother appended line. we keep growing")

