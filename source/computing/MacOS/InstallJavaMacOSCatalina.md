# Installing Java on MacOS 10.15 Catalina


First we need to install java. This is easiest done with brew: 

	brew cask install java

Not sure if the following two steps are necessary 

	brew tap adoptopenjdk/openjdk

	brew cask install adoptopenjdk8

Then, we need the command ant

	brew install ant

After installing ant, a message was shown: 

For the system Java wrappers to find this JDK, symlink it with
  sudo ln -sfn /usr/local/opt/openjdk/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk.jdk

openjdk is keg-only, which means it was not symlinked into /usr/local,
because macOS already provides this software and installing another version in
parallel can cause all kinds of trouble.

If you need to have openjdk first in your PATH run:
	echo 'export PATH="/usr/local/opt/openjdk/bin:$PATH"' >> ~/.bash_profile 

For compilers to find openjdk you may need to set:

 	export CPPFLAGS="-I/usr/local/opt/openjdk/include"
