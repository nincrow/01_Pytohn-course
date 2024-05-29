import os
import shutil

path = "folder"

try:
    #os.remove(path)    delete files
    #os.rmdir(path)     delete empty directory
    shutil.rmtree(path) #delete a directory containig files
except FileNotFoundError:
    print("The file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path +" was deleted")