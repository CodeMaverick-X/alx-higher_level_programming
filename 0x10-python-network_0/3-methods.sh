#!/bin/bash
# displays all the http methods a server will accept
curl -isLX OPTIONS $1 | grep 'Allow:' | cut -d ':' -f2 | | sed 's/^ //'
