'''
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        last = head
        if not head:
            return(None)
        length = 1
        while(last.next):
            last = last.next
            length+=1
        last.next = head
        k = k%length
        end = head
        for i in range(length - k - 1):
            end = end.next
        start = end.next
        end.next =None
        return(start)
