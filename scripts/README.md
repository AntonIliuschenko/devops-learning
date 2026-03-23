# My scripts, just for practice
* **isdockeractive.sh** # check if docker active, if active - print "active", if not - print "not active"
* **arguments.sh** # real magic, help to understand how to pass the arguments inside script
** **#!/usr/bin/env bash
	echo "First argument: $1"
	echo "All arguments: $@"
	echo "How many arguments: $#" **

x@WQ2WS:~/projects/devops-learning/scripts$ ./arguments.sh user docker git
						First argument: user
						All arguments: user docker git
						How many arguments: 3

