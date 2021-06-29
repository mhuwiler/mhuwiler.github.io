---
title: Prevent an application from updating
permalink: /computing/MacOS/AppNoUpdate
layout: single
sidebar:
  nav: "computing"
---

There exists a very elegant and drastic trick to prevent an application from updating: 

	sudo chflags -R schg /Applications/Some.app


Veto write access to disc! 

Big broder is watching you 
