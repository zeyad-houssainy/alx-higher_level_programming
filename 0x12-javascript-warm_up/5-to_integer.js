#!/usr/bin/node
if (process.argv[2] && !isNaN(process.argv[2])) {
  console.log(`My number: ${process.argv[2]}`);
} else {
  console.log('Not a number');
}
