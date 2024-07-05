/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function (tokens) {
  stack = [];
  operators = ["+", "-", "*", "/"];
  
  for (var i = 0; i < tokens.length; i++) {
    if (operators.includes(tokens[i])) {
      // Evaluate elpression
      r = parseInt(stack.pop());
      l = parseInt(stack.pop());
      result = perform_operation(tokens[i], l, r);
      stack.push(result);
    } else {
      // Push integer to stack
      stack.push(parseInt(tokens[i]));
    }
  }
  return stack.pop()
};

var perform_operation = function (operator, l, r) {
  switch (operator) {
    case "+":
      return l + r;
      break;
    case "-":
      return l - r;
      break;
    case "*":
      return l * r;
      break;
    case "/":
      return Math.trunc(l / r);
      break;
  }
};
