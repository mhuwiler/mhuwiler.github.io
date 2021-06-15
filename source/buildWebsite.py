#!/usr/bin/env python

import os
import sys
import shutil


sourcedirectory = "source/"
destinationdirectory="content/"
basedir = "/Users/mhuwiler/coding/mhuwiler.github.io/"

urlbase="https://mhuwiler.github.io/"

debug = True



def copyFolderContent(sourcedir, destdir, navfile, indent, instance): 
	for item in os.listdir(basedir+sourcedir): 
		#print item
		source = os.path.join(sourcedir, item)
		src = basedir+source
		if (debug): print src
		destination = os.path.join(destdir, item)
		dest = basedir+destination
		if (os.path.isdir(src)): 
			if (debug): print "\tmaking directory{}".format(dest)
			os.system("mkdir -p "+dest)
			title = ""
			try: 
				with open(src+"/title.txt") as titlefile: 
					titlecontent = titlefile.readlines()
					assert(len(titlecontent) == 1), "ERROR: Please make sure the file 'title.txt' in {} contains only a single line.".format(src)
					title = titlecontent[0].strip("\n")
			except: 
				title = item
			navfile.write(indent*"  "+"- title: "+title+"\n")
			navfile.write(indent*"  "+"  children: "+"\n")
			copyFolderContent(source, destination, navfile, indent+1, instance)
		elif (os.path.isfile(src)): 
			if (".md" in item): # only copy .md files
				if (debug): print "\tcopying file: {} to: {}".format(src, dest)
				destinationfile = open(dest, "w")
				with open(src, "r") as infile:
					content = infile.readlines()

					# writing the header for navigation
					destinationfile.write("---\n")
					destinationfile.write("title: {}\n".format("\"Title\""))
					destinationfile.write("permalink: {}\n".format("/"+destination))
					destinationfile.write("sidebar:\n  nav: \"{}\"\n".format(instance))
					destinationfile.write("---\n")

					for line in content: 
						destinationfile.write(line)
				destinationfile.close()

				navfile.write(indent*"  "+"- title: \""+item+"\"\n")
				navfile.write(indent*"  "+"  url: "+destination+"\n")

		else: 
			print "Error: {} is not a content file nor a directory!".format(src)

	# Add as an entry to the menu 
	
	#shutil.copy(folder, "../data")


if __name__ == "__main__":

	navigationfile = open(basedir+"_data/navigation.yml", "w")

	os.system("mkdir -p "+basedir+destinationdirectory)
	for item in os.listdir(basedir+sourcedirectory): 
		source = os.path.join(sourcedirectory, item)
		destination = os.path.join(destinationdirectory, item)
		print item
		if (os.path.isdir(basedir+source)): 
			navigationfile.write(item+":\n")
			indentation = 1
			os.system("mkdir -p "+basedir+destination)
			copyFolderContent(source, destination, navigationfile, indentation, item)

	navigationfile.close()


