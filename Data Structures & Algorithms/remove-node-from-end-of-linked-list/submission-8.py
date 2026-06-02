# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rec(self, root, k):
        if not root:
            return

        root.next = self.rec(root.next, k)

        k[0] -= 1
        
        if k[0] == 0:
            return root.next

        return root    
           

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head = self.rec(head, [n])
        return head