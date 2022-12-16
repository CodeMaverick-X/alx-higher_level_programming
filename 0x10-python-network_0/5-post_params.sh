#!/bin/bash
# use post to send request with cur
curl -sL -d "email=test@gmail.com&subject=I will always be here for PLD" -X POST "$1"
