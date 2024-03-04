const word = "kosi";
let newWord = word.split("");
newWord = newWord.reverse();
newWord = newWord.join("");

console.log(newWord);

// with space in the split and join
const sentence = "James is a man";
let newSentence = sentence.split(" ");
newSentence = newSentence.reverse();
newSentence = newSentence.join(" ");

console.log(newSentence);

// without space in the split and join
const groupSentence = "Fat cat jumped the mat";
let reversedGroupSentence = groupSentence.split("");
reversedGroupSentence = reversedGroupSentence.reverse();
reversedGroupSentence = reversedGroupSentence.join("");

console.log(reversedGroupSentence);

const country = "Choose a sentence";
let newCountry = country.replace("sentence", "country");
console.log(newCountry);

// [{'value': 'choose'}, {'value': 'an'}, {'value': 'answer'}]

const group4 = "Choose an answer";
let group4Array = group4.split(" ");

for (let i = 0; i < group4Array.length; i++) {
  group4Array[i] = { value: group4Array[i] };
}

console.log(group4Array);

// STRING METHODS

let text = "HELLO WORLD";
let char = text.charAt(0);

let alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
let length = alphabets.length;

const name = "W3Schools";
let letter = name.at(2);

let characters = "HELLO WORLD";
let charIndex = characters[0];

// This will not work
let any_variable = "HELLO WORLD";
any_variable[0] = "A";

let list = "Apple, Banana, Kiwi";
let part = list.slice(7, 13);
part = list.slice(-12);
part = list.slice(-12, -6);

let string = "Lemon, Apple, Orange";
let str_part = string.substring(7, 13);
str_part = string.substr(7, 6);
str_part = string.substr(-4);

let text1 = "Hello World!";
let text2 = text1.toUpperCase();

let str1 = "Hello";
let str2 = "World";
let str3 = str1.concat(" ", str2);

let word1 = "      Hello World!      ";
let word2 = word1.trim();

let value1 = "     Hello World!     ";
let value2 = value1.trimStart();

word1 = "     Hello World!     ";
word2 = word1.trimEnd();

let textToPad = "7";
let padded = textToPad.padStart(4, "0");

textToPad = "15";
padded = textToPad.padStart(4, "x");

textToPad = "4";
padded = textToPad.padEnd(4, "0");
