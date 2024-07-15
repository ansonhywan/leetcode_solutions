/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function (l1, l2) {
  res_list = new ListNode(0, null);
  traverser = res_list;
  carry_bit = 0;
  while (l1 || l2 || carry_bit) {
    v1 = l1 ? l1.val : 0;
    v2 = l2 ? l2.val : 0;
    sum = v1 + v2 + carry_bit;
    carry_bit = Math.trunc(sum / 10);
    digit = sum % 10;

    traverser.next = new ListNode(digit, null);
    traverser = traverser.next;
    l1 = l1 ? l1.next : null;
    l2 = l2 ? l2.next : null;
  }

  return res_list.next;
};
