(function () {
  "use strict";

  const currentEl = document.getElementById("current");
  const historyEl = document.getElementById("history");
  const buttonsEl = document.querySelector(".buttons");
  const themeToggle = document.getElementById("themeToggle");

  let current = "0";      // 현재 입력 중인 숫자
  let previous = null;    // 이전 피연산자
  let operator = null;    // 선택된 연산자 (÷ × − +)
  let justEvaluated = false;

  const OPS = {
    "÷": (a, b) => (b === 0 ? null : a / b),
    "×": (a, b) => a * b,
    "−": (a, b) => a - b,
    "+": (a, b) => a + b,
  };

  function render() {
    currentEl.textContent = current;
    if (previous !== null && operator) {
      historyEl.textContent = `${format(previous)} ${operator}`;
    } else {
      historyEl.textContent = "";
    }
  }

  function format(n) {
    if (n === "Error") return n;
    const num = Number(n);
    if (!isFinite(num)) return "Error";
    // 소수점 오차 정리 후 필요없는 0 제거
    return parseFloat(num.toPrecision(12)).toString();
  }

  function inputDigit(d) {
    if (current === "Error") current = "0";
    if (justEvaluated) {
      current = "0";
      justEvaluated = false;
    }
    if (d === ".") {
      if (!current.includes(".")) current += ".";
    } else if (current === "0") {
      current = d;
    } else {
      current += d;
    }
  }

  function chooseOperator(op) {
    if (current === "Error") return;
    if (operator && previous !== null && !justEvaluated) {
      compute();
    } else {
      previous = current;
    }
    operator = op;
    justEvaluated = false;
    current = "0";
    highlightOperator(op);
  }

  function compute() {
    if (operator === null || previous === null) return;
    const a = Number(previous);
    const b = Number(current);
    const result = OPS[operator](a, b);
    current = result === null ? "Error" : format(result);
    previous = null;
    operator = null;
    justEvaluated = true;
    highlightOperator(null);
  }

  function clearAll() {
    current = "0";
    previous = null;
    operator = null;
    justEvaluated = false;
    highlightOperator(null);
  }

  function deleteLast() {
    if (current === "Error" || justEvaluated) {
      current = "0";
      justEvaluated = false;
      return;
    }
    current = current.length > 1 ? current.slice(0, -1) : "0";
  }

  function percent() {
    if (current === "Error") return;
    current = format(Number(current) / 100);
  }

  function highlightOperator(op) {
    document
      .querySelectorAll(".op")
      .forEach((b) => b.classList.toggle("selected", b.dataset.value === op));
  }

  buttonsEl.addEventListener("click", (e) => {
    const btn = e.target.closest("button");
    if (!btn) return;
    const { action, value } = btn.dataset;

    if (action === "operator") chooseOperator(value);
    else if (action === "equals") compute();
    else if (action === "clear") clearAll();
    else if (action === "delete") deleteLast();
    else if (action === "percent") percent();
    else if (value !== undefined) inputDigit(value);

    render();
  });

  // 키보드 지원
  const keyMap = { "/": "÷", "*": "×", "-": "−", "+": "+" };
  document.addEventListener("keydown", (e) => {
    const k = e.key;
    if (/[0-9]/.test(k)) inputDigit(k);
    else if (k === ".") inputDigit(".");
    else if (keyMap[k]) chooseOperator(keyMap[k]);
    else if (k === "Enter" || k === "=") {
      e.preventDefault();
      compute();
    } else if (k === "Backspace") deleteLast();
    else if (k === "Escape") clearAll();
    else if (k === "%") percent();
    else return;
    render();
  });

  // 테마 토글 + 저장
  function applyTheme(theme) {
    const light = theme === "light";
    document.body.classList.toggle("light", light);
    themeToggle.textContent = light ? "☀️" : "🌙";
  }

  applyTheme(localStorage.getItem("calc-theme") || "dark");

  themeToggle.addEventListener("click", () => {
    const next = document.body.classList.contains("light") ? "dark" : "light";
    applyTheme(next);
    localStorage.setItem("calc-theme", next);
  });

  render();
})();
