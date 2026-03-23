#!/bin/bash

if systemctl is-active --quiet $1; then
	echo "$1 is running"
else
	echo "$1 is down"
fi
