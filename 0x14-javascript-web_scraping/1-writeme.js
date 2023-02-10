#!/usr/bin/node
const fileName = process.argv[2];
const data = process.argv[3];
const print = console.log;

const fs = require('fs');

fs.writeFile(fileName, data, {
  encoding: 'utf8',
  flag: 'w'
},
(err) => {
  if (err) {
    print(err);
  }
});
