const word = "kosi";
let newWord = word.split("");
newWord = newWord.reverse();
newWord = newWord.join("");

// console.log(newWord);

// with space in the split and join
const sentence = "James is a man";
let newSentence = sentence.split(" ");
newSentence = newSentence.reverse();
newSentence = newSentence.join(" ");

// console.log(newSentence);

// without space in the split and join
const groupSentence = "Fat cat jumped the mat";
let reversedGroupSentence = groupSentence.split("");
reversedGroupSentence = reversedGroupSentence.reverse();
reversedGroupSentence = reversedGroupSentence.join("");

// console.log(reversedGroupSentence);

const country = "Choose a sentence";
let newCountry = country.replace("sentence", "country");
// console.log(newCountry);

// [{'value': 'choose'}, {'value': 'an'}, {'value': 'answer'}]

const group4 = "Choose an answer";
let group4Array = group4.split(" ");

for (let i = 0; i < group4Array.length; i++) {
  group4Array[i] = { value: group4Array[i] };
}

// console.log(group4Array);

// STRING METHODS

let text = "HELLO WORLD";
let char = text.charAt(2);
// console.log(char);

let alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
let length = alphabets.length;
// console.log(length);

const name = "W3Schools";
let letter = name.at(2);
// console.log(letter);

let characters = "HELLO WORLD";
let charIndex = characters[0];
// console.log(charIndex);

// This will not work
let any_variable = "HELLO WORLD";
any_variable[0] = "t";
// console.log(any_variable[0]);

let list = "Apple, Banana, Kiwi";
let part = list.slice(7, 13);
// console.log(part);

part = list.slice(-12);
// console.log(part);

part = list.slice(-12, -6);
// console.log(part);

let string = "Lemon, Apple, Orange";
let str_part = string.substring(7, 13);
// console.log({ str_part }, 74);
// console.log({ string }, 75);
str_part = string.slice(7, 13);
// console.log({ str_part }, 77);

str_part = string.substr(7, 6);
// console.log(str_part);

str_part = string.substr(-4);
// console.log(str_part);

let text1 = "Hello Group 2!";
let text2 = text1.toUpperCase();
// console.log(text2);

let str1 = "Hello";
let str2 = "World";
let str3 = str1.concat(" ", str2);
// console.log(str3);

let word1 = "      Hello Group 2!      ";
let word2 = word1.trim();
// console.log(word2);

let value1 = "     Hello World!     see";
let value2 = value1.trimStart();
// console.log(value2);

word1 = "see     Hello World!     ";
word2 = word1.trimEnd();
// console.log(word2);

let textToPad = "7";
let padded = textToPad.padStart(4, "0");
// console.log(padded);

textToPad = "15";
padded = textToPad.padStart(4, "x");
// console.log(padded);

textToPad = "4";
padded = textToPad.padEnd(4, "0");
// console.log(padded);
