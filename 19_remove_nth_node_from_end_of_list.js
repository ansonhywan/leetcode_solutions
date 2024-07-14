/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function (head, n) {
  // Use two pointers to find n nodes from end of LL
  dummy = new ListNode(0, head);
  slow = dummy;
  fast = head;
  while (n != 0) {
    fast = fast.next;
    n -= 1;
  }

  // Bring fast pointer to the end of LL
  // Slow pointer will end up n spots behind tail node
  while (fast != null) {
    fast = fast.next;
    slow = slow.next;
  }

  // Remove node at slow pointer
  slow.next = slow.next.next;

  return dummy.next;
};
