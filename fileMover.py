#   fileMover
#   =========
#
#  Autor:    schaerphix
#  Date:     05.12.2022
#  Revision: V1.1
#
#  LICENSE:  GNU General Public License v3.0  
#
#  Description:
#  The fileMover help you to move a huge number of files from A to B.
#


#   imports
import progressBar
from os import listdir
from os.path import isfile, join
import shutil
from time import sleep
import sys

#   classes
class Parameter:

    def __init__(self):
        self.name = "fileMover"
        self.version = "V1.1"
        self.author = "schaerphix"

    def ParaPrint(self):
        #print(sys.argv)
        print("filemover    Version: %s      Author: %s"%(self.version,self.author))


#   Funtions

#   MAIN
def main():
    # initial
    paras = Parameter()
    paras.ParaPrint()

    # preparation
    if len(sys.argv) > 1:
        folder_orig = sys.argv[1]
    else:
        folder_orig = input("Origin folder: ")
    if len(sys.argv) > 2:
        folder_dest= sys.argv[2]
    else:
        folder_dest = input("destination folder: ")
    files = [f for f in listdir(folder_orig) if isfile(join(folder_orig, f))]
    if folder_dest[len(folder_dest) - 1] != '\\' or folder_dest[len(folder_dest) - 1] != '/':
        folder_dest = folder_dest + '/'
    doit = "j"
    if doit == "j" or doit == "J":
         # Initial call to print 0% progress
        progressBar.printProgressBar(0, len(files), prefix='Progress:', suffix='Complete', length=50)
        for i, item in enumerate(files):
            shutil.copyfile(folder_orig + "/" + item, folder_dest + item)
            # Update Progress Bar
            progressBar.printProgressBar(i + 1, len(files), prefix='Progress:', suffix='Complete', length=50)

    # END
    print("\nIt was my pleasure! See you soon!\n")



if __name__ == '__main__':
    main()
