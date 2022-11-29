#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  let i;
  for (i in list) {
    if (list[i] === searchElement) {
      count++;
    }
  }
  return count;
};
