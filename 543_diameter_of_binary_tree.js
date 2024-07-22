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

var diameterOfBinaryTree = function (root) {
  let dia = 0;
  function dfs(root) {
    if (root === null) return -1;
    let l_h = dfs(root.left);
    let r_h = dfs(root.right);
    dia = Math.max(dia, l_h + r_h + 2);
    return 1 + Math.max(l_h, r_h);
  }
  dfs(root);
  return dia;
};
