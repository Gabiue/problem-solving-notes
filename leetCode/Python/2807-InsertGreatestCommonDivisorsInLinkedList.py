# 2807. Insert Greatest Common Divisors in Linked List (Medium)
# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/
# Between every two adjacent nodes, insert a new node whose value
# is the GCD of those two nodes, and return the head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from math import gcd

class Solution:
    def insertGreatestCommonDivisors(self, head: ListNode | None) -> ListNode | None:
        cur = head
        while cur.next:
            node = ListNode(gcd(cur.val, cur.next.val), cur.next)
            cur.next = node
            cur = node.next  # skip the new node, move to the next original one
        return head
