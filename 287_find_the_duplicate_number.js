/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function (nums) {
  s = 0;
  f = 0;
  while (true) {
    s = nums[s];
    f = nums[nums[f]];
    if (s === f) break;
  }

  s2 = 0;
  while (true) {
    s = nums[s];
    s2 = nums[s2];
    if (s === s2) return s;
  }
};
