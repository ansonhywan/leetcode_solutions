/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function (nums) {
  l = 0;
  r = nums.length - 1;

  while (l <= r) {
    m = Math.trunc((l + r) / 2);

    if (nums[m + 1] < nums[m]) {
      // Inflection point is at this index m
      return nums[m + 1];
    }

    first_elem = nums[0];
    if (nums[m] >= first_elem) {
      // The inflection point is between m and r
      l = m + 1;
    } else {
      // The inflection point is between l and m
      r = m - 1;
    }
  }
  return m === nums.length - 1 ? nums[0] : nums[m + 1];
};
