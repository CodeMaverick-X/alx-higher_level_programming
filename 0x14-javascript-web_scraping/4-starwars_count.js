#!/usr/bin/node
const url = process.argv[2];
const print = console.log;

const request = require('request');

request(url, (error, response, body) => {
  if (error) {
    print(error);
  } else {
    let count = 0;
    for (const film of JSON.parse(body).results) {
      for (const character of film.characters) {
        if (character.includes('18')) {
          count++; // i hate triangles too
        }
      }
    }
    print(count);
  }
});
