#!/usr/bin/node
const url = process.argv[2];
const print = console.log;

const request = require('request');

request(url, (error, response, body) => {
  if (error) {
    print(error);
  }
  print('code:', response.statusCode);
});
