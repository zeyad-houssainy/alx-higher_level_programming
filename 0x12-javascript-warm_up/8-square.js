#!/usr/bin/node
if (process.argv[2] && !isNaN(process.argv[2])) {
  for (let i = 0; i < process.argv[2]; i++) {
    for (let j = 0; j < process.argv[2]; j++) {
      console.log(process.argv[2]);
    }
    console.log('\n')
  }
  } else {
    console.log('Missing size');
  }
