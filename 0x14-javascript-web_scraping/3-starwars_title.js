#!/usr/bin/node
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
const print = console.log;

const request = require('request');

request(url, (error, response, body) => {
  if (error) {
    print(error);
  } else {
    print(JSON.parse(body).title);
  }
});
