#!/usr/bin/node
if (process.argv[2] && !NaN(process.argv[2])) {
  for (let i = 0; i < process.argv[2]; i++) { console.log(process.argv[2]); }
} else {
  console.log('Missing size');
}
