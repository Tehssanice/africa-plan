const hdsStudents = ["Ezekiel", "Theresa", "Cosy", "Koach"];

function myCallbackFn(theName, theIndex, theArray) {
  // console.log(`${theName} is on index ${theIndex} in the array: ${theArray}`);
}

hdsStudents.forEach(myCallbackFn);

hdsStudents.forEach(function (value, index, array) {
  // console.log(value);
  // console.log(index);
  // console.log(array);
});

hdsStudents.forEach((value, index, array) => {
  // console.log(value);
  // console.log(index);
  // console.log(array);
});

console.log("\n\n"); // new line

const APStudents = ["Ezekiel", "Theresa", "Cosy", "Koach"];
function APSCallbackfn(item, index, myArray) {
  if (index == 0) {
    return item.toLowerCase();
  }
  if (index == myArray.length - 1) {
    return item.toUpperCase();
  }
  return { value: item };
}

const newValue = APStudents.map(APSCallbackfn);
// console.log(newValue);

const newValue1 = APStudents.map(function (item, index, myArray) {
  if (index == 0) {
    return item.toLowerCase();
  }
  if (index == myArray.length - 1) {
    return item.toUpperCase();
  }
  return { value: item };
});

const newValue2 = APStudents.map((item, index, myArray) => {
  if (index == 0) {
    return item.toLowerCase();
  }
  if (index == myArray.length - 1) {
    return item.toUpperCase();
  }
  return { value: item };
});

const claraArray = ["Tessa", "Koach", "Kosi", "David"];

const claraArrayFunction = (theItem) => {
  if (theItem == "Tessa") {
    return {
      name: theItem,
      status: "active",
    };
  } else {
    return {
      name: theItem,
      status: "inactive",
    };
  }
};
// console.log(claraArray.map(claraArrayFunction));

// OR THE FOREACH METHOD BELOW

let newArray = [];

claraArray.forEach((theItem) => {
  if (theItem == "Tessa") {
    newArray.unshift({
      name: theItem,
      status: "active",
    });
    return;
  }
  newArray.push({
    name: theItem,
    status: "inactive",
  });
});
// console.log(newArray);

const user = [
  {
    id: "0398823885859",
    name: "jane",
    number: 896533,
  },

  {
    id: "235377869948746",
    name: "Mott",
    number: 373579,
  },

  {
    id: "7584867388",
    name: "plane",
    number: 236439,
  },

  {
    id: "456798767890",
    name: "Lank",
    number: 434578,
  },

  {
    id: "09876678938765",
    name: "Sam",
    number: 147854,
  },

  {
    id: "9700974345",
    name: "Chike David",
    number: 424345,
  },
];

// console.log(users[2].name);

const chikeDavid = users.find(function (item) {
  return item.name == "Chike David";
});

// console.log(chikeDavid);
// console.log(chikeDavid.name);

const usersusers = users.concat(users);
const usersusers1 = [...usersusers];

// console.log(usersusers1);

users.find((item) => {
  if (item.number.toString().includes("4345")) {
    console.log(item);
  }
});

// console.log(chikeDavid3);
// console.log("44".includes("4"));

const username = ["tessa", "theo", "koach"];

const filteredUsers = username.filter().includes("o");
console.log(filteredUsers);
