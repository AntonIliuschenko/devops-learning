#!/bin/bash

if systemctl is-active --quiet docker; then
	echo "Docker is running"
else
	echo "Docker is down"
fi
