#!/usr/bin/node
// Fix: Convert CommonJS module to ES module
exports.esrever = function (list) {
  const newList = [];
  for (const i of list) {
    newList.unshift(i);
  }
  return newList;
};
