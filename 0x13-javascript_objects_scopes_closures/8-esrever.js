#!/usr/bin/node
exports.esrever = function (list) {
  const lst = [];
  let j = 0;
  let i;
  for (i = list.length - 1; i >= 0; i--) {
    lst[j] = list[i];
    j++;
  }
  return lst;
};
