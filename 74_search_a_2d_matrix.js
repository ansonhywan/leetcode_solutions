/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function (matrix, target) {
  num_rows = matrix.length;
  num_cols = matrix[0].length;

  row = 0;
  l = 0;
  r = num_rows - 1;
  // Search for correct row first
  while (l <= r) {
    m = Math.trunc((l + r) / 2);
    if (target === matrix[m][0]) {
      row = m;
      break;
    }
    if (target < matrix[m][0]) {
      r = m - 1;
    } else {
      l = m + 1;
    }
  }
  row = Math.trunc((l + r) / 2);

  // Now search for value in the row
  l = 0;
  r = num_cols;
  while (l <= r) {
    m = Math.trunc((l + r) / 2);
    if (target === matrix[row][m]) {
      return true;
    }
    if (target < matrix[row][m]) {
      r = m - 1;
    } else {
      l = m + 1;
    }
  }
  return false;
};
