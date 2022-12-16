#!/bin/bash
# script that takes in a URL, sends a request to that URL
# and displays the size of the body of the response
text=$(curl -s -I "$1" | grep Content-Length)
IFS=' '
read -r -a strarr <<< "$text"
echo "${strarr[1]}"
