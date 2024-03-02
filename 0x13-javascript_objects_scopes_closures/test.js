// export class Person{
//     constructor(name, age){
//         this.name = name;
//         this.age = age;
//     }
// }

const myObject = {
  name: 'Zeyad',
  greet () {
    console.log(`Hello, my name is ${this.name}`);
  }
};

myObject.greet();
