#!/usr/bin/env python

import os
import sys
import shutil
import yaml
import glob


sourcedirectory = "source/"
destinationdirectory="content/"
basedir = "/Users/mhuwiler/coding/mhuwiler.github.io/"

urlbase="http://127.0.0.1:4000/" #"https://mhuwiler.github.io/"

CONFIGDELIMITER="#<conf>" #"#!header"

debug = True



def copyFolderContent(sourcedir, destdir, navfile, indent, instance): 
	for item in os.listdir(basedir+sourcedir): 
		#print item
		source = os.path.join(sourcedir, item)
		src = basedir+source
		if (debug): print src
		destination = destdir+"_"+item #os.path.join(destdir, item)
		dest = basedir+destination
		if (os.path.isdir(src)): 
			if (debug): print "\tmaking directory{}".format(dest)
			#os.system("mkdir -p "+dest)
			title = ""
			try: 
				with open(src+"/title.txt") as titlefile: 
					titlecontent = titlefile.readlines()
					assert(len(titlecontent) == 1), "ERROR: Please make sure the file 'title.txt' in {} contains only a single line.".format(src)
					title = titlecontent[0].strip("\n")
			except: 
				title = item
			navfile.write(indent*"  "+"- title: "+title+"\n")
			if (os.path.isfile(src+"/index.md")): # There is a index.md file in the folder 
				destinationfile = open(dest+"_index.md", "w")
				with open(src+"/index.md", "r") as infile:
					content = infile.readlines()
					config = {}
					if (content[0].startswith(CONFIGDELIMITER)): # the first line starts with the header marker 
						config = yaml.safe_load(content[0][len(CONFIGDELIMITER):])
						content.pop(0) # remove the header line 
						print config

					# writing the header for navigation
					destinationfile.write("---\n")
					if ("title" in config): 
						destinationfile.write("title: {}\n".format(config["title"]))
					destinationfile.write("permalink: {}\n".format("/"+destination))
					destinationfile.write("layout: single\n")
					destinationfile.write("sidebar:\n  nav: \"{}\"\n".format(instance))
					if ("toc" in config and config["toc"]==1): destinationfile.write("toc: true\n")
					destinationfile.write("---\n")

					for line in content: 
						destinationfile.write(line)
				destinationfile.close()
				navfile.write(indent*"  "+"  url: "+destination+"\n")

			navfile.write(indent*"  "+"  children: "+"\n")
			copyFolderContent(source, destination, navfile, indent+1, instance)
		elif (os.path.isfile(src)): 
			if (".md" in item): # only copy .md files
				destination = source.replace("source/", "").replace(".md", "")
				if (debug): print "\tcopying file: {} to: {}".format(src, dest)
				destinationfile = open(dest, "w")
				with open(src, "r") as infile:
					content = infile.readlines()
					config = {}
					if (content[0].startswith(CONFIGDELIMITER)): # the first line starts with the header marker 
						config = yaml.safe_load(content[0][len(CONFIGDELIMITER):])
						content.pop(0) # remove the header line 
						print config

					# writing the header for navigation
					destinationfile.write("---\n")
					if ("title" in config): 
						destinationfile.write("title: {}\n".format(config["title"]))
					destinationfile.write("permalink: {}\n".format("/"+destination))
					destinationfile.write("layout: single\n")
					destinationfile.write("sidebar:\n  nav: \"{}\"\n".format(instance))
					if ("toc" in config and config["toc"]==1): destinationfile.write("toc: true\n")
					destinationfile.write("---\n")

					for line in content: 
						destinationfile.write(line)
				destinationfile.close()

				if ("navtitle" in config): 
					navtitle = config["navtitle"]
				else: 
					navtitle = item.replace(".md", "")
				navfile.write(indent*"  "+"- title: \""+navtitle+"\"\n")
				navfile.write(indent*"  "+"  url: "+destination+"\n")

		else: 
			print "Error: {} is not a content file nor a directory!".format(src)

	# Add as an entry to the menu 
	
	#shutil.copy(folder, "../data")


if __name__ == "__main__":

	navigationfile = open(basedir+"_data/navigation.yml", "w")

	os.system("mkdir -p "+basedir+destinationdirectory)
	navigationfile.write("main:\n")
	for src in glob.glob(basedir+sourcedirectory+"*/index.md"): 
		print src
		destination = src.replace(basedir+sourcedirectory, "")
		dest = destination.replace("/", "_")
		destination = destination.replace("/index.md", "")
		#if (destination.startswith("home")): destination = destination[:len("home")]
		if(destination == ""): destination = "/"
		navtitle = destination
		destinationfile = open(dest, "w")
		with open(src, "r") as infile:
			content = infile.readlines()
			config = {}
			if (content[0].startswith(CONFIGDELIMITER)): # the first line starts with the header marker 
				config = yaml.safe_load(content[0][len(CONFIGDELIMITER):])
				content.pop(0) # remove the header line 
				print config

			# writing the header for navigation
			destinationfile.write("---\n")
			if ("title" in config): 
				destinationfile.write("title: {}\n".format(config["title"]))
			destinationfile.write("permalink: {}\n".format("/"+destination))
			destinationfile.write("layout: single\n")
			#destinationfile.write("sidebar:\n  nav: \"{}\"\n".format(instance))
			if ("toc" in config and config["toc"]==1): destinationfile.write("toc: true\n")
			destinationfile.write("---\n")

			if ("navtitle" in config): 
				navtitle = config["navtitle"]

			for line in content: 
				destinationfile.write(line)
		destinationfile.close()

		navigationfile.write(" - title: \"{}\"\n".format(navtitle))
		navigationfile.write("   url: {}\n".format(destination))

	print "Regular website building"
	for item in os.listdir(basedir+sourcedirectory): 
		source = os.path.join(sourcedirectory, item)
		destination = destinationdirectory+item #os.path.join(destinationdirectory, item)
		print item
		if (os.path.isdir(basedir+source)): 
			navigationfile.write(item+":\n")
			indentation = 1
			#os.system("mkdir -p "+basedir+destination)
			copyFolderContent(source, destination, navigationfile, indentation, item)

	navigationfile.close()


