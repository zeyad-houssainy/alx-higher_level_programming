#!/usr/bin/node
const array = Array.from(new Set(process.argv.slice(2))).sort((a, b) => b - a);
if (array.length == 0 || array.length == 1) {
  console.log(0);
} else {
  console.log(array[1]);
}
