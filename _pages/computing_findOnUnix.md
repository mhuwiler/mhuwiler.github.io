---
title: Find a in subfolders
permalink: /computing/findOnUnix
layout: single
sidebar:
  nav: "computing"
---

On Unix systems, it is extremely easy to find all files matching a given pattern in the subfolder of the current directory: 

	find . -name "foo*"

This command supports wildcards. 

Alternativley, instead of the dot a directory name can be provided. 

