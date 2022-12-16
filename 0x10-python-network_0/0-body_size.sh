#!/bin/bash
# script that takes in a URL, sends a request to that URL
text=$(curl -s -I "$1" | grep Content-Length)
read -r -a strarr <<< "$text"
echo "${strarr[1]}"
