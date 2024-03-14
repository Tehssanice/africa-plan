const display = document.getElementById("display");
const display2 = document.getElementById("display2");
const powerButton = document.querySelector(".power-btn");
const offOn = document.querySelector("[data-off-on]");

const addToInput = (value) => {
  if (value === "." && display.value.includes(".")) {
    return;
  }
  if (display.value.length < display.maxLength || value === ".") {
    display.value += value;
  }
};

const operator = (value) => {
  let plus = display.value + value;
  return (display2.value = plus);
};

function toggleOnOff() {
  const buttons = document.querySelectorAll("button");
  buttons.forEach((button) => {
    if (button !== offOn) {
      button.classList.toggle("disabled");
    }
  });
  if (offOn.textContent === "OFF") {
    offOn.textContent = "ON";
    display.value = "";
    display2.value = "";
    display.placeholder = "";
  } else {
    offOn.textContent = "OFF";
    display.placeholder = "0";
  }
}

offOn.addEventListener("click", () => {
  toggleOnOff();
});

const calculateResult = () => {
  try {
    const result = eval(display2.value + display.value);
    display.value = result;
  } catch (error) {
    display.value = "Error";
  }
};

const backspace = () => {
  display.value = display.value.slice(0, -1);
};

const clearDisplay = () => {
  display.value = "";
};

const clearDisplay2 = () => {
  display2.value = "";
};

display.addEventListener("input", function () {
  this.value = this.value.replace(/\D/g, "");
});
