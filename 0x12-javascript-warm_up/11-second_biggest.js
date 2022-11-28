#!/usr/bin/node
const process = require('process');
let max = 0;
let sMax = 0;
let i;
let j = 0;

for (i in process.argv) {
  if (j >= 2) {
    i = parseInt(process.argv[i]);
    if (i >= max) {
      sMax = max;
      max = i;
    }
  }
  j++;
}
console.log(sMax);
