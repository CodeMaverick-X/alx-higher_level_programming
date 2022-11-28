#!/usr/bin/node
const process = require('process');

let i = 0;
let j;
let flag = 0;
for (j in process.argv) {
  if (i >= 2) {
    console.log(process.argv[j]);
    flag = 1;
  }
  i++;
}

if (flag === 0) {
  console.log('No argument');
}
