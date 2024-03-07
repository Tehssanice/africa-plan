const claraArray = ["silas", "victor", "clara"];
// ------- USING MAP -------

let newArrayMap = claraArray.map((name) => {
  if (name == "clara") {
    return {
      name,
      status: "active",
    };
  }
  return {
    name,
    status: "inactive",
  };
});

console.log(newArrayMap);

// ------- USING FOREACH ------- //

// ---- WITH IF_ELSE ------- //
let newArrayForEach1 = [];
claraArray.forEach((name) => {
  if (name == "silas") {
    newArrayForEach1.unshift({
      name,
      status: "active",
    });
  } else {
    newArrayForEach1.push({
      name,
      status: "inactive",
    });
  }
});
console.log(newArrayForEach1);

// ---- WITH TENARY OPARATOR ------- //
let newArrayForEach2 = [];
claraArray.forEach((name) => {
  // condition ? doTrue : doFalse
  name == "silas"
    ? newArrayForEach2.unshift({
        name,
        status: "active",
      })
    : newArrayForEach2.push({
        name,
        status: "inactive",
      });
});
console.log(newArrayForEach2);
// ------APPROACH TWO: FOREACH WITH RETURN GUARD -------
let newArrayForEach3 = [];
claraArray.forEach((name) => {
  if (name == "silas") {
    newArrayForEach3.unshift({
      name,
      status: "active",
    });
    return;
  }
  newArrayForEach3.push({
    name,
    status: "inactive",
  });
});
console.log(newArrayForEach3);

// ------APPROACH TWO: FOREACH WITH RETURN GUARD 2 -------

let newArrayForEach4 = [];
claraArray.forEach((name) => {
  if (name == "silas") {
    return newArrayForEach4.unshift({
      name,
      status: "active",
    });
  }
  newArrayForEach4.push({
    name,
    status: "inactive",
  });
});
console.log(newArray1);

// ------ MAP SYNTAXs  ONE -------
const resultclara = claraArray.map((name, idx) => {
  const performance = name + "-" + idx;
  return {
    name,
    status: "active",
    performance,
  };
});
// ------ MAP SYNTAXs  TWO -------
const resultclara2 = claraArray.map((name) => ({ name, status: "active" }));

// ------ USINGS MAP SYNTAXs  EXAMPLE -------
const oArray = [
  {
    name: "theodore", // 0 -- sileasIndex -1
    score: 20,
  },
  {
    name: "silas", // 1 -- claraIndex -1   theodoreIndex + 1
    score: 40,
  },
  {
    name: "clara", // 2 -- victorIndex -1 silasIndex + 1
    score: 60,
  },
  {
    name: "victor", // claraIndex + 1
    score: 80,
  },
];

const resultclara3 = oArray.map((item, idx, students) => {
  let performance = 0;
  const itemBelow = students[idx + 1];
  if (itemBelow) {
    performance = (item.score / itemBelow.score) * 100;
  }
  return {
    name: item.name,
    performance,
  };
});

// ------ USINGS MAP SYNTAXs  FIVE -------
// students[idx + 1]?.score ?? 0
// returnValueWhenDefined??returnValueWhenUndefined
const resultclara4 = oArray.map((item, idx, students) => {
  const performance = (item.score / (students[idx + 1]?.score ?? 0)) * 100;
  return {
    name: item.name,
    performance,
  };
});
console.log("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
console.log(resultclara4);
