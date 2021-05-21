#!/usr/bin/env python

import os
import sys
import shutil


sourcedir = "."
destdir="../data"



def copyFolderContent(sourcedir, destdir): 
	for item in os.listdir(sourcedir): 
		#print item
		itempath = os.path.join(sourcedir, item)
		print itempath
		if (os.path.isdir(itempath)): 
			currentdir = os.path.join(destdir, item)
			print "making directory", currentdir
			os.system("mkdir -p "+currentdir)
			copyFolderContent(itempath, currentdir)
		elif (os.path.isfile(itempath)): 
			destinationfile = open(os.path.join(destdir, item), "w")
			with open(itempath, "r") as infile:
				content = infile.readlines()
				destinationfile.write("---\nheader\n---\n")
				for line in content: 
					destinationfile.write(line)
			destinationfile.close()

		else: 
			print "Error: {} is not file nor directory!".format(itempath)

	# Add as an entry to the menu 
	
	#shutil.copy(folder, "../data")


if __name__ == "__main__":

	os.system("mkdir -p "+destdir)
	copyFolderContent(sourcedir, destdir)


