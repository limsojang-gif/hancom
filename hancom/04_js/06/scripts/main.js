

const flavor = document.querySelector("#flavor");
const result = document.querySelector("#result");

document.querySelector("#check").addEventListener("click", () => {

  if (flavor.value === "choco") {
    result.textContent = " 초코 너무 달아";
  } else if (flavor.value === "vanilla") {
    result.textContent = "바닐라 좋아";
  } else {
    result.textContent = "딸기 는 과일";
  }
});