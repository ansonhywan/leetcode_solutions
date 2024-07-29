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
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function (root, k) {
  let res = [];
  dfs_to_k(root, k, res);
  return res[k - 1];
};

function dfs_to_k(root, k, res) {
  if (!root) return;
  dfs_to_k(root.left, k, res);
  res.push(root.val);
  dfs_to_k(root.right, k, res);
  return;
}
