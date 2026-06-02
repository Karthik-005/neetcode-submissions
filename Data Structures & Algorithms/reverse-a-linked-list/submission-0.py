# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode], prev = None) -> Optional[ListNode]:
        if not head :
            return prev

        nxt = head.next
        head.next = prev

        return self.reverseList(nxt, head)    


