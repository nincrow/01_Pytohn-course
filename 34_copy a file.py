# copyfile() =  copies contents of a file
# copy() =      copyfile() + permission mode + destination can be a direstory
# copy2() =     copy() + copies metadata (file's creation and modification times)

import shutil

shutil.copy('test.txt','copy.txt') #src,dst

