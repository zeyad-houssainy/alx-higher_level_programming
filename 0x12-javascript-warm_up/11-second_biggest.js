#!/usr/bin/node
const array = [...new Set(process.argv.slice(2).sort().map(Number))];
if (array.length === 0 || array.length === 1) {
  console.log(0);
} else {
  console.log(array[array.length - 2]);
}
