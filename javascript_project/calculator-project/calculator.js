const display = document.getElementById("display");
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

const buttons = document.querySelectorAll("button");

offOn.addEventListener("click", () => {
  buttons.forEach((button) => {
    if (button !== offOn) {
      button.classList.toggle("disabled");
    }
    togglePower();
  });
});

const calculateResult = () => {
  try {
    const result = eval(display2.value + display.value);
    display.value = result;
  } catch (error) {
    display.value = "Error";
  }
};

const togglePower = () => {
  const isCalculatorOn = !display.disabled;

  if (isCalculatorOn) {
    display.disabled = true;
    display.value = "";
    powerButton.textContent = "OFF";
  } else {
    display.disabled = false;
    powerButton.textContent = "ON";
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
