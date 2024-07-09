/**
 * @param {number} target
 * @param {number[]} position
 * @param {number[]} speed
 * @return {number}
 */
var carFleet = function (target, position, speed) {
  pos_spd = [];
  for (i = 0; i < position.length; i++) {
    pos_spd.push([position[i], speed[i], (target - position[i]) / speed[i]]);
  }

  pos_spd.sort(function (a, b) {
    return b[0] - a[0];
  });

  stack = [];
  for (const [pos, spd, ttt] of pos_spd) {
    stack.push(ttt);

    if (stack.length > 1 && stack.at(-1) <= stack.at(-2)) {
      stack.pop();
    }
  }

  return stack.length;
};
