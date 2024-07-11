/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
  // Find inflection points using binary search
  l = 0;
  r = nums.length - 1;
  inf_index = 0;
  while (l <= r) {
    m = Math.trunc((l + r) / 2);
    if (nums[m + 1] < nums[m]) {
      // Found inflection point at index m
      break;
    }
    if (nums[m] >= nums[0]) {
      l = m + 1;
    } else {
      r = m - 1;
    }
  }
  inf_index = m;

  // Now perform binary search on either left or right on inf_index to find the target value
  if (target < nums[0]) {
    l = inf_index + 1;
    r = nums.length - 1;
  } else if (target > nums[0]) {
    l = 0;
    r = inf_index;
  } else {
    return 0;
  }
  while (l <= r) {
    m = Math.trunc((l + r) / 2);
    if (nums[m] === target) {
      return m;
    }
    if (target < nums[m]) {
      r = m - 1;
    } else {
      l = m + 1;
    }
  }
  return -1;
};
