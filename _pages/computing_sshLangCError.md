---
title: LANG = "C" error in ssh 
permalink: /computing/sshLangCError
layout: single
sidebar:
  nav: "computing"
---

It can happen (namely on MacOS) that certain commands typed in a remote SSH session trigger the following error: 

	perl: warning: Please check that your locale settings:
	LANGUAGE = (unset),
	LC_ALL = (unset),
	LC_CTYPE = "UTF-8",
	LANG = "C"
    are supported and installed on your system.
	perl: warning: Falling back to the standard locale ("C").

This error is not a misconfiguration of the remote, but results in a miscommunication between the remote and the local SSH client. 

There exist several ways to straighten out this issue, documented here: https://stackoverflow.com/questions/2499794/how-to-fix-a-locale-setting-warning-from-perl

As on often has control over the local computer, but not necessarily to the remote one, the convenient fix to implement is the third one from the first answer: stop SSH from sending the environment variables, by commenting the line 'SendEnv LANG LC_*' in the file /etc/ssh/ssh_config. 

	sudo vim /etc/ssh/ssh_config

And make the line (49 in my case) look like: 

	#SendEnv LANG LC_*

This should fix the issue for any remote SSH that you try connecting to in the future. 
