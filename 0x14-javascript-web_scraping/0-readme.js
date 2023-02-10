#!/usr/bin/node
const fileName = process.argv[2];
const print = console.log;

const fs = require('fs');

fs.readFile(fileName, 'utf8', (err, data) => {
  if (err) {
    print(err);
  }
  print(data);
});
