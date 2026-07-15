(function () {
  "use strict";

  // ===== State =====
  var currentInput = "0"; // string being typed
  var previousInput = null; // number stored before operator
  var operator = null; // "+", "-", "*", "/"
  var justEvaluated = false; // last action was "="
  var history = [];

  var OP_SYMBOL = { "+": "+", "-": "−", "*": "×", "/": "÷" };

  // ===== DOM =====
  var currentEl = document.getElementById("current");
  var expressionEl = document.getElementById("expression");
  var historyListEl = document.getElementById("history-list");
  var historyEmptyEl = document.getElementById("history-empty");
  var keypad = document.querySelector(".calc-keypad");

  // ===== Rendering =====
  function formatNumber(n) {
    if (!isFinite(n)) return "Error";
    // avoid floating point noise, keep up to 10 significant digits
    var rounded = Math.round((n + Number.EPSILON) * 1e10) / 1e10;
    var str = String(rounded);
    if (str.length > 14 && str.indexOf("e") === -1) {
      str = rounded.toPrecision(12).replace(/\.?0+$/, "");
    }
    return str;
  }

  function render() {
    currentEl.textContent = currentInput;
    if (previousInput !== null && operator) {
      expressionEl.textContent =
        formatNumber(previousInput) + " " + OP_SYMBOL[operator];
    } else {
      expressionEl.innerHTML = "&nbsp;";
    }
    // highlight active operator
    Array.prototype.forEach.call(
      keypad.querySelectorAll(".key-op"),
      function (btn) {
        btn.classList.toggle(
          "active",
          operator !== null && btn.getAttribute("data-op") === operator && !justEvaluated
        );
      }
    );
  }

  // ===== Core operations =====
  function compute(a, b, op) {
    switch (op) {
      case "+": return a + b;
      case "-": return a - b;
      case "*": return a * b;
      case "/": return b === 0 ? NaN : a / b;
    }
    return b;
  }

  function inputDigit(d) {
    if (justEvaluated) {
      currentInput = d;
      justEvaluated = false;
    } else if (currentInput === "0") {
      currentInput = d;
    } else {
      if (currentInput.replace(/[-.]/g, "").length >= 14) return;
      currentInput += d;
    }
  }

  function inputDecimal() {
    if (justEvaluated) {
      currentInput = "0.";
      justEvaluated = false;
      return;
    }
    if (currentInput.indexOf(".") === -1) currentInput += ".";
  }

  function chooseOperator(nextOp) {
    var value = parseFloat(currentInput);
    if (operator && previousInput !== null && !justEvaluated) {
      var result = compute(previousInput, value, operator);
      if (!isFinite(result)) return showError();
      previousInput = result;
      currentInput = formatNumber(result);
    } else {
      previousInput = value;
    }
    operator = nextOp;
    justEvaluated = false;
    currentInput = currentInput; // keep display; start fresh on next digit
    // mark that the next digit should replace current
    startFresh = true;
  }

  var startFresh = false;

  function inputDigitWrapped(d) {
    if (startFresh) {
      currentInput = "0";
      startFresh = false;
    }
    inputDigit(d);
  }

  function inputDecimalWrapped() {
    if (startFresh) {
      currentInput = "0";
      startFresh = false;
    }
    inputDecimal();
  }

  function equals() {
    if (operator === null || previousInput === null) return;
    var value = parseFloat(currentInput);
    var result = compute(previousInput, value, operator);
    if (!isFinite(result)) return showError();

    var exprStr =
      formatNumber(previousInput) +
      " " + OP_SYMBOL[operator] + " " +
      formatNumber(value);
    var resultStr = formatNumber(result);

    addHistory(exprStr, resultStr);

    currentInput = resultStr;
    previousInput = null;
    operator = null;
    justEvaluated = true;
    startFresh = false;
  }

  function clearAll() {
    currentInput = "0";
    previousInput = null;
    operator = null;
    justEvaluated = false;
    startFresh = false;
  }

  function negate() {
    if (currentInput === "0" || currentInput === "Error") return;
    currentInput =
      currentInput.charAt(0) === "-"
        ? currentInput.slice(1)
        : "-" + currentInput;
  }

  function percent() {
    var value = parseFloat(currentInput);
    currentInput = formatNumber(value / 100);
    justEvaluated = false;
  }

  function backspace() {
    if (justEvaluated || startFresh) return;
    if (currentInput.length <= 1 || (currentInput.length === 2 && currentInput.charAt(0) === "-")) {
      currentInput = "0";
    } else {
      currentInput = currentInput.slice(0, -1);
    }
  }

  function showError() {
    currentInput = "Error";
    previousInput = null;
    operator = null;
    justEvaluated = true;
    render();
  }

  // ===== History =====
  function addHistory(expr, result) {
    history.unshift({ expr: expr, result: result });
    if (history.length > 20) history.pop();
    renderHistory();
  }

  function renderHistory() {
    historyListEl.innerHTML = "";
    if (history.length === 0) {
      var empty = document.createElement("li");
      empty.className = "history-empty";
      empty.textContent = "아직 계산 기록이 없어요.";
      historyListEl.appendChild(empty);
      return;
    }
    history.forEach(function (item) {
      var li = document.createElement("li");
      li.className = "history-item";
      li.setAttribute("role", "button");
      li.setAttribute("tabindex", "0");
      li.innerHTML =
        '<div class="hi-expr">' + item.expr + '</div>' +
        '<div class="hi-result">' + item.result + '</div>';
      li.addEventListener("click", function () {
        reuseResult(item.result);
      });
      li.addEventListener("keydown", function (e) {
        if (e.key === "Enter" || e.key === " ") {
          e.preventDefault();
          reuseResult(item.result);
        }
      });
      historyListEl.appendChild(li);
    });
  }

  function reuseResult(result) {
    if (result === "Error") return;
    currentInput = result;
    previousInput = null;
    operator = null;
    justEvaluated = true;
    startFresh = false;
    render();
  }

  // ===== Event wiring =====
  keypad.addEventListener("click", function (e) {
    var btn = e.target.closest("button.key");
    if (!btn) return;

    if (btn.hasAttribute("data-num")) {
      if (currentInput === "Error") clearAll();
      inputDigitWrapped(btn.getAttribute("data-num"));
    } else if (btn.hasAttribute("data-op")) {
      if (currentInput === "Error") return;
      chooseOperator(btn.getAttribute("data-op"));
    } else {
      var action = btn.getAttribute("data-action");
      if (action === "clear") clearAll();
      else if (action === "negate") negate();
      else if (action === "percent") percent();
      else if (action === "decimal") {
        if (currentInput === "Error") clearAll();
        inputDecimalWrapped();
      } else if (action === "equals") equals();
    }
    render();
  });

  document.getElementById("clear-history").addEventListener("click", function () {
    history = [];
    renderHistory();
  });

  // Keyboard support
  document.addEventListener("keydown", function (e) {
    var k = e.key;
    if (k >= "0" && k <= "9") {
      if (currentInput === "Error") clearAll();
      inputDigitWrapped(k);
    } else if (k === ".") {
      if (currentInput === "Error") clearAll();
      inputDecimalWrapped();
    } else if (k === "+" || k === "-" || k === "*" || k === "/") {
      if (currentInput === "Error") return;
      chooseOperator(k);
    } else if (k === "Enter" || k === "=") {
      e.preventDefault();
      equals();
    } else if (k === "Backspace") {
      backspace();
    } else if (k === "Escape") {
      clearAll();
    } else if (k === "%") {
      percent();
    } else {
      return;
    }
    render();
  });

  // init
  render();
  renderHistory();
})();
