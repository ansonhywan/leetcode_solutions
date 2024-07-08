/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function (head) {
  // Slow-Fast (Tortoise and Hare) pointer method

  (slow = head), (fast = head);

  while (fast != null && fast.next != null) {
    slow = slow.next;
    fast = fast.next.next;
    if (slow === fast) {
      return true;
    }
  }
  return false;
};

/*
var hasCycle = function(head) {
    // Use Set to track visited nodes
    // Traverse LL to check if we already visited
    
    if (head === null) {
        return false
    }

    seen = new Set([head])
    while (head.next != null) {
        if (seen.has(head.next)) {
            return true
        } else {
            seen.add(head.next)
            head = head.next
        }
    }
    return false
};
*/
