#!/usr/bin/node
const process = require('process');

const length = process.argv.length;

if (length < 3) {
  console.log('No Argument');
} else if (length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
