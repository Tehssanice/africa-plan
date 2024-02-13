// function sum(a, b) {
//   return a * b;
// }

// const value = sum(5, 6);
// console.log(value);

// const runFaith2 = (name, group) => {
//   return `${name}, ${group}`;
//   return name + " " + group;
// };

// const groupValue = runFaith2("Faith", "Group 1");

// console.log(groupValue);

// // Caling a function as a prarameter
// const callFunction = (anyFunction) => {
//   const result = anyFunction(30, 50);
//   console.log(result);
// };

// function callFunction(anyFunction) {
//   const result = anyFunction(30, 50);
//   console.log(result);
// }

// function Add(c, d) {
//   return c + d;
// }

// function subtract(e, f) {
//   return e - f;
// }
// callFunction(subtract);

// //calling a function multiple times [loops]

// //for loop

// for (let i = 0; i <= 5; i++) {
//   //   //to display just the odd numbers
//   if (i % 2 !== 0) console.log(i);
// }

// for (let i = 4; i >= 1; i--) {
//   console.log(i);
// }

// //define function doubleNum
// function doubleNum(i) {
//   return i * 2;
// }

// //use doubleNum
// for (let i = 1; i < 6; i = doubleNum(i)) {
//   console.log(i);
// }

// // //arrays
// const result = [40, 24, "Theodore", "Seyi", "Land"];

// for (let i = 0; i < result.length; i++) {
//   console.log(result[i]);
// }

// const myArray = Array(11);
// console.log(myArray.length);

// const cars = ["Bentley", "Porshe", "BMW", "Toyota"];

// //for each loop
// cars.forEach(function (item) {
//   console.log(item);
// });

// result.forEach((value) => {
//   console.log(value);
// });

// // for of
// for (const items of cars) {
//   console.log(items);
// }

// // do while loop
// // while loop

let num = 6;
console.log(num++);
num++;
console.log(num);
