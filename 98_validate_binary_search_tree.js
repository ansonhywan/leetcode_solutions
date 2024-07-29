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
var isValidBST = function (root) {
  return validNode(root, -Infinity, Infinity);
};

function validNode(root, min, max) {
  if (!root) return true;

  if (root.val <= min) return false;
  if (root.val >= max) return false;

  const res_l = validNode(root.left, min, root.val);
  const res_r = validNode(root.right, root.val, max);

  return res_l && res_r;
}
