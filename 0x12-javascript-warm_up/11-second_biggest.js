#!/usr/bin/node
const process = require('process');
let max = 0;
let sMax = 0;
let i;

for (i in process.argv) {
  i = process.argv[i];
  if (i >= max) {
    sMax = max;
    max = i;
  }
}
console.log(sMax);
