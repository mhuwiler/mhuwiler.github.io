#!/usr/bin/env python

import os
import sys
import shutil


sourcedirectory = "."
destinationdirectory="../data"

urlbase="https://mhuwiler.github.io/"

debug = True



def copyFolderContent(sourcedir, destdir, navfile, indent): 
	for item in os.listdir(sourcedir): 
		#print item
		source = os.path.join(sourcedir, item)
		if (debug): print source
		destination = os.path.join(destdir, item)
		if (os.path.isdir(source)): 
			if (debug): print "\tmaking directory{}".format(destination)
			os.system("mkdir -p "+destination)
			title = ""
			try: 
				with open(source+"/title.txt") as titlefile: 
					titlecontent = titlefile.readlines()
					print titlecontent
					assert(len(titlecontent) == 1), "ERROR: Please make sure the file 'title.txt' in {} contains only a single line.".format(source)
					title = titlecontent[0].strip("\n")
			except: 
				title = item
			navfile.write(indent*"\t"+"- title: "+title+"\n")
			navfile.write(indent*"\t"+"  children: "+"\n")
			copyFolderContent(source, destination, navfile, indent+1)
		elif (os.path.isfile(source)): 
			if (".md" in item): # only copy .md files
				if (debug): print "\tcopying file: {} to: {}".format(source, destination)
				destinationfile = open(destination, "w")
				with open(source, "r") as infile:
					content = infile.readlines()
					destinationfile.write("---\nheader\n---\n")
					for line in content: 
						destinationfile.write(line)
				destinationfile.close()

				navfile.write(indent*"\t"+"- title: \""+item+"\"\n")
				navfile.write(indent*"\t"+"  url: "+item+"\n")

		else: 
			print "Error: {} is not a content file nor a directory!".format(source)

	# Add as an entry to the menu 
	
	#shutil.copy(folder, "../data")


if __name__ == "__main__":

	navigationfile = open("../navigation.yml", "w")

	os.system("mkdir -p "+destinationdirectory)
	for item in os.listdir(sourcedirectory): 
		source = os.path.join(sourcedirectory, item)
		destination = os.path.join(destinationdirectory, item)
		if (os.path.isdir(source)): 
			navigationfile.write(item+":\n")
			indentation = 1
			os.system("mkdir -p "+destination)
			copyFolderContent(source, destination, navigationfile, indentation)

	navigationfile.close()


