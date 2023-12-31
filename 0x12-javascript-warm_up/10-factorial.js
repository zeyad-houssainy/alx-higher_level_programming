#!/usr/bin/node

function factorial (number) {
  if (Number(number === 0) || Number(number === 1) || isNaN(number)) {
    return 1;
  } else {
    return (Number(number * factorial(number - 1)));
  }
}

console.log(factorial(process.argv[2]));
