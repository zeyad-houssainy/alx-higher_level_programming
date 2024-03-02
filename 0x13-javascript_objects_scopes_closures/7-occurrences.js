#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((count, currentItem) => {
    return currentItem === searchElement ? count + 1 : count;
  }, 0);
};
