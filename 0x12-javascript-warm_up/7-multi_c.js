#!/usr/bin/node
const process = require('process');

const number = parseInt(process.argv[2]);
const message = 'C is fun';
let i;

if (isNaN(number)) {
  console.log('Not a number');
} else {
  for (i = 0; i < number; i++) {
    console.log(message);
  }
}
