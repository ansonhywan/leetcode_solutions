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
 * @return {number[]}
 */
var rightSideView = function (root) {
  if (!root) return [];

  res = [];
  q = [];
  q.push(root);

  while (q.length > 0) {
    level_len = q.length;
    right_most = null;
    for (let i = 0; i < level_len; i++) {
      const n = q.shift();

      // The last node in the level is the right most
      right_most = n;

      // Push next level to exploration queue
      if (n.left) q.push(n.left);
      if (n.right) q.push(n.right);
    }
    res.push(right_most.val);
  }
  return res;
};
