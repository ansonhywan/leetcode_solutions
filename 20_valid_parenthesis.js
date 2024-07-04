/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  mapping = { "}": "{", ")": "(", "]": "[" };
  stack = [];

  for (const c of s) {
    if (c in mapping) {
      if (stack[stack.length - 1] === mapping[c]) {
        stack.pop();
      } else {
        return false;
      }
    } else {
      stack.push(c);
    }
  }

  return stack.length === 0;
};
