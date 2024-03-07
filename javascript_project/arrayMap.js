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
console.log(newArray);
