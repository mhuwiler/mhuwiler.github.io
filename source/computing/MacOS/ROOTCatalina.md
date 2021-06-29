#<conf>{"title": "Build ROOT on MacOS 10.15 Catalina", "navtitle": "Build ROOT", "toc":1}

The way to build ROOT changes all so often (at almost every system update or major ROOT version change), as a lot of options have defaults that might change or break. For building ROOT on MacOS 10.15, with MacPorts, the optimal solution looks like this: 


## Downloading ROOT

To download ROOT, it is best to follow the instructions here: 


## Building ROOT agaisnt custom installed Python 

First, make sure to install python with MacPorts according to these instructions: 

Then, (assuming the default python version has been set to the one installed with macports) ROOT needs to be built against it. By default, the location of python should be recognised by ROOT's build system, but in my case (MacOS 10.15 Catalina, python 2.7 from MacPorts, cmake 6.16.3 from MacPorts, and ROOT 6.18.04 downloaded from github) it did not work out. The solution was to provide manually the PYTHON_LIBRARY and PYTHON_INCLUDE_DIR variables to the ones corresponding to the MacPorts install of python. By default, MacPorts installs everything into /opt/local, and then it is a matter of finding the library and include dir of the wished (if more than one) version. 

The command looks something like: 

	cmake -Droofit=ON -Dtmva=ON -Drpath=ON -DPYTHON_INCLUDE_DIR=/opt/local/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7 -DPYTHON_LIBRARY=/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/libpython2.7.dylib -Dcxx17=ON -Droot7=ON -DCMAKE_CXX_STANDARD=17 ../root

Where you can set the desired additional options from: https://root.cern.ch/building-root

In this case, I wanted to make sure TMVA and RooFit are built (-Droofit=ON -Dtmva=ON), but you should turn on the packages you need. The defaults can also change from one version to the other, so it is best to always activate the desired options, even if it should be activated by default. 

The option -Drpath=ON can be needed in case you want to compile software against your installation fo ROOT, so it is recommended to turn it on. 

I also wanted to enable C++ 2017 syntax (-Dcxx17=ON -DCMAKE_CXX_STANDARD=17), as well as preliminary ROOT7 features (-Droot7=ON, requiring C++2017). 


If the configuration works fine, one can finally build ROOT: 


After a successful build, the freshly built ROOT can be activated by sourcing the script: 

	source bin/thisroot.sh

In order to not need to do it everytime you want to open ROOT, you can put a line in the .bash_profile: 

	source /path/to/ROOT/build/dir/bin/thisroot.sh

This way, root will default to this version. 


also put export PATH='/opt/local/Library/Frameworks/Python.framework/Versions/2.7/bin:'$PATH in bash_profile (for jupyter and ipython)

Also talk about: 
	port select --list python
	port notes python27
	sudo port select --set python python27
    sudo port select --set python2 python27

And write python installation with MacPorts

