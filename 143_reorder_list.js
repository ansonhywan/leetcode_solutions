/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {void} Do not return anything, modify head in-place instead.
 */
var reorderList = function (head) {
  // Find middle of LL
  // Use fast and slow pointer
  // Fast pointer will end up finding tail
  // Slow pointer will end up finding middle
  middle = head;
  tail = head.next;
  while (tail && tail.next) {
    middle = middle.next;
    tail = tail.next.next;
  }

  // Reverse links in second half of LL
  traverser = middle.next;
  middle.next = null;
  prev = null;
  while (traverser) {
    temp = traverser.next;
    traverser.next = prev;
    prev = traverser;
    traverser = temp;
  }

  // Build new LL
  traverser1 = head;
  traverser2 = prev;
  while (traverser2) {
    temp1 = traverser1.next;
    temp2 = traverser2.next;
    traverser1.next = traverser2;
    traverser2.next = temp1;
    traverser1 = temp1;
    traverser2 = temp2;
  }
};
