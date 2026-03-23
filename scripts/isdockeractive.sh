#!/bin/bash

if systemctl is-active --quiet docker; then
	echo "docker is running"
else
	echo "docker is down"
fi
