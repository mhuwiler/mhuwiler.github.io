#!/usr/bin/env python

import os
import sys
import shutil


sourcedir = "."
destdir="../data"



def copyFolderContent(sourcedir, destdir): 
	for item in os.listdir(sourcedir): 
		#print item
		source = os.path.join(sourcedir, item)
		print source
		destination = os.path.join(destdir, item)
		if (os.path.isdir(source)): 
			print "making directory", destination
			os.system("mkdir -p "+destination)
			copyFolderContent(source, destination)
		elif (os.path.isfile(source)): 
			destinationfile = open(destination, "w")
			with open(source, "r") as infile:
				content = infile.readlines()
				destinationfile.write("---\nheader\n---\n")
				for line in content: 
					destinationfile.write(line)
			destinationfile.close()

		else: 
			print "Error: {} is not file nor directory!".format(source)

	# Add as an entry to the menu 
	
	#shutil.copy(folder, "../data")


if __name__ == "__main__":

	os.system("mkdir -p "+destdir)
	copyFolderContent(sourcedir, destdir)


