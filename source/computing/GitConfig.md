#!header{title: "Configuring git", navtitle: "git configuration", toc:0}

In order to use git, you will need to provide some basic information: 



Also, in my opinion, the default merge behaviour is not optimal, so I recommend disabling fast-forward merge: 

	git config --global --add merge.ff false

More about why this twak might be beneficial is explained here: https://mijingo.com/blog/preventing-non-fast-forward-git-merges

##Git workflow

Regarding the workflow to use for git projects, an idea is: 

https://nvie.com/posts/a-successful-git-branching-model/

