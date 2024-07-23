/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function (p, q) {
  if (!p && !q) {
    // Base case
    return true;
  }
  if (p && q && p.val === q.val) {
    // Both not null and equal values
    const res_l = isSameTree(p.left, q.left);
    const res_r = isSameTree(p.right, q.right);
    return res_l && res_r;
  } else {
    return false;
  }
};
