# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        result = []
        current = head

        while current:
            result.append(current.val)
            current = current.next
        result.sort()

        dummy = ListNode(0)
        current = dummy

        for value in result:
            current.next = ListNode(value)
            current = current.next
            
        return dummy.next



        