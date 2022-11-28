#!/usr/bin/node
const process = require('process');

let number;

number = parseInt(process.argv[2]);

if (isNaN(number)) {
  console.log('Not a number');
  return;
} else
  console.log(`My number: ${number}`);