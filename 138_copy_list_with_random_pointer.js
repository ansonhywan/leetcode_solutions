/**
 * // Definition for a _Node.
 * function _Node(val, next, random) {
 *    this.val = val;
 *    this.next = next;
 *    this.random = random;
 * };
 */

/**
 * @param {_Node} head
 * @return {_Node}
 */
var copyRandomList = function (head) {
  // First pass, create node copies
  traverser = head;
  node_map = new Map();
  while (traverser != null) {
    new_node = new _Node(traverser.val, null, null);
    node_map.set(traverser, new_node);
    traverser = traverser.next;
  }

  // Second pass, create links
  traverser = head;
  while (traverser != null) {
    new_node = node_map.get(traverser);
    new_node.next = node_map.get(traverser.next) || null;
    new_node.random = node_map.get(traverser.random) || null;
    traverser = traverser.next;
  }

  return node_map.get(head);
};
