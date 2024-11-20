# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1
    
        merge = list1
        a = list1.next
        b = list2
        m = merge

        while a and b:
            if b.val < a.val:
                m.next = b
                b = b.next
                m = m.next

            else:
                m.next = a
                a = a.next
                m = m.next

        if a:
            m.next = a
        if b:
            m.next = b
        m.next = a if a else b

        return merge




            