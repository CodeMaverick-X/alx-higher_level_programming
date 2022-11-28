#!/usr/bin/node
const process = require('process');

const number = parseInt(process.argv[2]);
let i;
let j;

if (isNaN(number)) {
  console.log('Missing size');
} else {
  for (i = 0; i < number; i++) {
    for (j = 0; j < number; j++) {
      process.stdout.write('X');
    }
    console.log();
  }
}
