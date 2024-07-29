/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var goodNodes = function (root) {
  return checkNode(root, root.val);
};

function checkNode(root, max) {
  if (!root) return 0;

  let res = 0;
  if (root.val >= max) {
    res = 1;
  } else {
    res = 0;
  }
  max = Math.max(max, root.val);

  res += checkNode(root.left, max);
  res += checkNode(root.right, max);

  return res;
}
