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
 * @return {boolean}
 */
var isBalanced = function (root) {
  if (root === null) return true;

  const l = dfs(root.left);
  const r = dfs(root.right);

  return l[0] && r[0] && Math.abs(l[1] - r[1]) <= 1 ? true : false;
};

var dfs = function (root) {
  if (root === null) return [true, -1];

  const l = dfs(root.left);
  const r = dfs(root.right);

  balanced = l[0] && r[0] && Math.abs(l[1] - r[1]) <= 1;
  h = Math.max(l[1], r[1]) + 1;

  return [balanced, h];
};
