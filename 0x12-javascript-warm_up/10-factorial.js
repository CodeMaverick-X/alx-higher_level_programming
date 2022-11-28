#!/usr/bin/node
const process = require('process');

const num1 = parseInt(process.argv[2]);

function fact (num) {
  if (num === 1 || num === 0) {
    return 1;
  }

  return num * fact(num - 1);
}

const n = fact(num1);
console.log(n);
