# 21. Merge Two Sorted Lists (Easy)
# https://leetcode.com/problems/merge-two-sorted-lists/
# Merge two sorted linked lists into one sorted list by relinking
# their nodes, and return the head of the merged list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        if not list1 or not list2:
            return list1 or list2
        if list1.val > list2.val:
            list1, list2 = list2, list1  # keep the smaller head in list1
        list1.next = self.mergeTwoLists(list1.next, list2)
        return list1
