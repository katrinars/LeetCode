# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst = []
        if not head or not head.next:
            return True
        curr = head
        while curr:
            lst.append(curr.val)
            curr = curr.next
        return lst == lst[::-1]
        
        