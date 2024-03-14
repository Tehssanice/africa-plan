// Callback
function myFirst(anyFn) {
  // anyFn("Day Good");
  const greeting = "Day Good";
  anyFn?.(greeting);
  // anyFn?.();
}

function mySecond() {
  console.log("Good bye");
}

function goodNight(message) {
  console.log(message);
}

//   myFirst(mySecond);
//   myFirst(goodNight);
//   myFirst();
// myFirst((message) =>{
//     console.log(message);
// });

//   const timeoutId = setTimeout(mySecond, 10000); // 10 seconds;
const timeoutId = setTimeout(() => {
  // myFirst(mySecond);
}, 10000); // 10 seconds;
// console.log(timeoutId);
clearTimeout(timeoutId);
// setTimeout(() => {
//     myFirst(mySecond);
// }, 10000);

const breakFast = (somto) => {
  setTimeout(() => {
    console.log("Breakfast Completed");
    somto?.();
  }, 3000);
};

const HDSClass1 = (somto) => {
  setTimeout(() => {
    console.log("Hordanso Class 1 Completed");
    somto?.();
  }, 10000);
};

const lunch = (after) => {
  setTimeout(() => {
    console.log("Lunch Completed");
    after?.();
  }, 2000);
};

const HDSClass2 = (after) => {
  setTimeout(() => {
    console.log("Hordanso Class 2 Completed");
    after?.();
  }, 2000);
};

const startToday = () => {
  breakFast(() => {
    HDSClass1(() => {
      lunch(() => {
        HDSClass2(() => {
          console.log("Day as ended");
        });
      });
    });
  });
};
// startToday();

// const intervalId = setInterval(()=>{
// console.log("Silas")
// }, 500)

// const clara = setTimeout(()=>{
//     // clearInterval(intervalId)
// }, 10000)

// clearTimeout(clara)

const displayCompletionPercent = (percent) => {
  console.log(percent, "%");
};
let time = 0;
const HDSClassDetails1 = (somto) => {
  const totalTimeForEating = 10000;
  let intervalForUpdate = 1000;

  /// callback as better here
  const id = setInterval(() => {
    time = time + intervalForUpdate;
    somto?.((time / totalTimeForEating) * 100);
  }, intervalForUpdate);

  setTimeout(() => {
    console.log("Hordanso Class 1 Completed");
    clearInterval(id);
  }, totalTimeForEating);
};

// HDSClassDetails1((numPercent)=>{
//     displayCompletionPercent(numPercent)
// })
