/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
var dailyTemperatures = function (temperatures) {
  result = Array(temperatures.length).fill(0);
  stack = [];

  for (const [i, temp] of temperatures.entries()) {
    while (stack.length > 0 && temp > stack.at(-1)[0]) {
      pop = stack.pop();
      result[pop[1]] = i - pop[1];
    }

    stack.push([temp, i]);
  }

  return result;
};
