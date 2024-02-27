console.log('HI');
const array = ['#1', 'Python is cool', 'JavaScript is amazing'];
for (i of array) {
  console.log(i);
}

let name = 'zeyad';
const age = 25;
const list = [];
list.push(name);
console.log(list);
list.push(age);
console.log(list);
console.log({} + []);
name = 'Habiba';
console.log(`${name} is good`);

console.log(isNaN('5')); // False y3ne howa number

// if (process.argv[2])
let x;
x = 1;
console.log(x);

if (Process.argv[2] && !isNaN(Process.argv[2])) {
  for (let i = 0; i < Process.argv[2]; i++) {
    console.log('C is fun');
  }
} else {
  console.log('mgesh rawam');
}

const squareSize = Number(Process.argv[2]);
if (Process.argv[2] && !isNaN(Process.argv[2])) {
  for (let i = 0; i < Process.argv[2]; i++) {
    console.log('X'.repeat(squareSize));
  }
}

function add (a, b) {
  return (parseInt(a) + parseInt(b));
}
console.log(add(Process.argv[2], Process.argv[3]));

function factorial (number) {
  if (Number(number) === 0 || Number(number) === 1 || isNaN(number)) {
    return 1;
  } else {
    return (Number(number * factorial(number - 1)));
  }
}
