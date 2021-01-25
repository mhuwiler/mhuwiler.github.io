layout: page
title: "Ceating folders in / under MacOS Catalina"
permalink: /MacOS/FoldersAtTheRoot

# Ceating folders in / under MacOS Catalina 

With MacOS 10.15 Catalina, the system volume has become read-only, and it is therefore not possible anymore to create folders at the root /. It is however possible to create a symbolic at / that points to some other folder with write persmission in the filesystem. 

To do so, one needs to add a line 'link 	some/folder/that/is/writable' in the file /etc/Synthetic.conf. link is the name of the symbolic that will be shown in / and the rest (separated by a tab!), is the path to the folder it points to, for instance /usr/local/somefolder. Note the absence of leading slash in the folder path. 

So it looks like this: 

	sudo vim etc/Synthetic.conf

And then add the following line to the file: 

	eos	usr/local/filesystem/eos


Credit for this goes to: https://apple.stackexchange.com/questions/371908/how-to-make-root-volume-writeable-again-in-catalina
