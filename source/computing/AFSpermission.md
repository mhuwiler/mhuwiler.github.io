# Giving permission to an AFS folder

Information taken from: https://information-technology.web.cern.ch/services/fe/afs/howto/configure-afs-access-rights

On AFS, permissions are managed differently from a regular unix file system. The permissions are displayed with the following command: 

	fs listacl

AFS has a lot of different levels of permissions, listed below: 

	r = “read” allows the named user to read the file content and to query file status.
	l = “lookup” allows the user to list the files and directories, to examine the ACL and to access the subdirectories.
	i = “insert” allows the user to add new files and directories.
	d = “delete” allows the user to remove files from a directory and to remove subdirectories, for which they have insert right.
	w = “write” allows the user to change the file content (and also to change the UNIX permission bits, see below).
	k = “lock” allows the user to use full-file advisory locks. (Note that there is no byte-range locking available in AFS.)
	a = “administer” allows the user to change the ACL of a directory.

In oder to make life easier, there also exist sets of predifined permissions that are close to those of unix file systems: 

	“read” corresponds to rl and provides read access;
	“write” corresponds to rlidwk and grants read and write access;
	“all” corresponds to rlidwka and gives full access;
	“none” removes all permissions for a user.
	
Inorder to give write permission to a given user, use the following command: 

	fs setacl -dir directory -acl username write

This will give the user username wrote permission to filder directory. 


### Give recursively permission to subdirectories

To give recursively permission to all subfolders, do the following: 

	afind directory/ -t d -e "fs setacl -dir {} -acl username write"

This should enable use username to write in all subdirectories of directory.