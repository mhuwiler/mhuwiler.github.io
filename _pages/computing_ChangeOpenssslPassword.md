---
title: Changing an openSSL password
permalink: /computing/ChangeOpenssslPassword
layout: single
sidebar:
  nav: "computing"
---

	openssl rsa -des3 -in myserver.key -out server.key.new
	chmod go-rw $HOME/.globus/userkey.pem
	export X509_USER_PROXY=~/.x509up_u`id -u`
	ssh-keygen -p -f ~/.ssh/id_dsa
