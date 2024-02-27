#!/usr/bin/node
const array = Array.from(new Set(process.argv.slice(2))).sort((a, b) => a - b);
console.log(array[1]);
