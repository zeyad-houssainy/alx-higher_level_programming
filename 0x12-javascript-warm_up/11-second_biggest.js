#!/usr/bin/node
const array = [...new Set(process.argv.slice(2).sort.map(Number))];
console.log(array.length === 0 || array.length === 1 ? 0 : array[-2]);
