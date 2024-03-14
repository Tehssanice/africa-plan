const users = [
  {
    id: "720357c8-4109-4610-b68e-1744c35813cc",
    isActive: true,
    age: 22,
    name: "Myrtle Thornton",
    gender: "female",
    company: "GEEKFARM",
    email: "myrtlethornton@geekfarm.com",
    phone: "+1 (990) 465-2715",
    favoriteFruit: "strawberry",
  },
  {
    id: "bb6e6f2e-2a8d-4dbc-94c4-979c74f131e0",
    isActive: false,
    name: "Chike David",
    gender: "female",
    age: 33,
    company: "SCHOOLIO",
    email: "caroledavid@schoolio.com",
    phone: "+1 (807) 501-3963",
    favoriteFruit: "banana",
  },
  {
    id: "c6f05816-1fd5-448a-8b11-3e761de683c3",
    isActive: true,
    name: "Suzette Clark",
    gender: "female",
    company: "INQUALA",
    age: 27,
    email: "suzetteclark@inquala.com",
    phone: "+1 (903) 489-2336",
    favoriteFruit: "apple",
  },
  {
    id: "5de18d34-b833-4f6f-8633-17465e9956c7",
    isActive: false,
    name: "Underwood Adkins",
    gender: "male",
    company: "GEEKOL",
    age: 27,
    email: "underwoodadkins@geekol.com",
    phone: "+1 (886) 518-2001",
    favoriteFruit: "strawberry",
  },
  {
    id: "b185dfde-737c-44fc-abae-29d2ed522af5",
    isActive: true,
    name: "Lydia Wallace",
    gender: "female",
    age: 24,
    company: "BIZMATIC",
    email: "lydiawallace@bizmatic.com",
    phone: "+1 (942) 580-3019",
    favoriteFruit: "banana",
  },
  {
    id: "2c57893f-515b-4c4d-91e1-2619867f376b",
    isActive: false,
    name: "Jeanette Simmons",
    gender: "female",
    age: 24,
    company: "ENTROFLEX",
    email: "jeanettesimmons@entroflex.com",
    phone: "+1 (845) 485-2909",
    favoriteFruit: "banana",
  },
  {
    id: "660937c2-8cbe-4ce6-8121-9a6c6e97e61f",
    isActive: false,
    name: "Walter Espinoza",
    age: 23,
    gender: "male",
    company: "EARTHMARK",
    email: "walterespinoza@earthmark.com",
    phone: "+1 (897) 558-2989",
    favoriteFruit: "banana",
  },
];

// const chikeDavid = users.find(function(item){
//     return item.name == "Chike David";
// });
const chikeDavid2 = users.find((item) => item.name == "Chike David");

// console.log(chikeDavid);
console.log(chikeDavid2);
// const chikeDavidMap = users.map((item)=>item.name == "Chike David");
// console.log(chikeDavidMap);
const chikeDavid3 = users.find((item) => item.phone == "+1 (807) 501-3963");
// console.log("tesa".includes("tse"));
// console.log(
//     ["tesa", "theo", 'koach'].includes("theo"));
const chikeDavid4 = users.find((item) => item.phone.includes("2715"));
const chikeDavidCompany = users.find((item) => item.company.toUpperCase() == "GEekFARm".toUpperCase());
// users.find((item)=>item.company.toLowerCase() == "GEekFARm".toLowerCase());
console.log("\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
console.log(chikeDavidCompany);

const suzetteClark = users.find((item) => item.gender == "female");
console.log("\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
console.log(suzetteClark);

const suzetteClark1 = users.find((item) => item.gender == "female" && item.favoriteFruit == "apple");
console.log("\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
console.log(suzetteClark1);
const suzetteClarkIdea = users.find((item) => item.id == "c6f05816-1fd5-448a-8b11-3e761de683c3");
console.log("\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
console.log(suzetteClarkIdea);

const filterUsers = users.filter((item) => item.id == "c6f05816-1fd5-448a-8b11-3e761de683c3");
console.log("\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
console.log(filterUsers);

const filterUsers1 = users.filter((item) => item.isActive == true);
console.log("\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
console.log(filterUsers1);
const usersName = ["tesa", "theo", "koach"];
const filterUsers2 = usersName.filter((item) => item.includes("o"));
const findUsers2 = usersName.find((item) => item.includes("o"));
console.log("\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
console.log(filterUsers2);
console.log(findUsers2);

const filterUsers3 = users.filter((item) => item.name.includes("o"));
const findUsers3 = users.find((item) => item.name.includes("o"));
console.log("\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
console.log(filterUsers3);
console.log(findUsers3);

const someUsers = users.some((item) => item.name.includes("o"));
console.log("\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
console.log(someUsers);

const everyUsers = users.every((item) => item.name.includes("o"));
console.log("\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
console.log(everyUsers);

const filterNumOfUsers = users.filter((item) => item.name.includes("o"));
console.log("\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
console.log(filterNumOfUsers.length);

const reduceUsers = users.reduce((acc, item) => {
  if (item.name.includes("o")) {
    acc = acc + 1;
  }
  return acc;
}, 0);
console.log("\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
console.log(reduceUsers);

const reduceUsersAgeSum = users.reduce((acc, item) => {
  // acc=acc+item.age;
  return acc + item.age;
}, 0);
console.log("\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
console.log(reduceUsersAgeSum);

const reduceUsersInfoSummary = users.reduce(
  (acc, item, currentIndex) => {
    // acc=acc+item.age;
    if (item.isActive) {
      acc.numActiveUsers = acc.numActiveUsers + 1;
    }
    if (item.gender == "female") {
      acc.numOfFemales = acc.numOfFemales + 1;
    }
    if (item.favoriteFruit == "banana") {
      acc.numOfBanana = acc.numOfBanana + 1;
    }

    acc.arrayOfNames = acc.arrayOfNames.concat(item.name);
    // acc.arrayOfNames= [item.name].concat(acc.arrayOfNames)
    // acc.arrayOfNames= [...acc.arrayOfNames, item.name]

    acc.listSeparatedByCommasCompany = acc.listSeparatedByCommasCompany.concat(
      currentIndex == 0 ? item.name : "," + item.name
    );
    //  acc.listSeparatedByCommasCompany = `${acc.listSeparatedByCommasCompany}${currentIndex==0?item.name:","+item.name}`;
    return acc;
  },
  {
    numActiveUsers: 0,
    numOfFemales: 0,
    numOfBanana: 0,
    arrayOfNames: [],
    listSeparatedByCommasCompany: "",
  }
);
console.log("\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
console.log(reduceUsersInfoSummary);
