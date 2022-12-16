#!/bin/bash
#omo
curl -isL $1 | grep 'Allow:' | cut -d ':' -f2 | | sed 's/^ //'
