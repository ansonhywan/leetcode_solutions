/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function (n) {
  var stack = [];
  var results = [];

  var recursion = function (open_count, closed_count) {
    // Base Case
    if (open_count === n && closed_count === n) {
      results.push(stack.join(""));
      return;
    }

    // General Case
    if (open_count < n) {
      stack.push("(");
      recursion(open_count + 1, closed_count);
      stack.pop();
    }
    if (closed_count < open_count) {
      stack.push(")");
      recursion(open_count, closed_count + 1);
      stack.pop();
    }
  };

  recursion(0, 0);
  return results;
};
