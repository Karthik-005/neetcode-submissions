# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rec(self, root, k, head):
        if not root:
            return

        self.rec(root.next, k, head)

        k[0] -= 1
        if k[0] == 1 and root == head:
            return head.next

        if k[0] == 0:
            print(1)
            root.next = root.next.next

        return root    

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head = self.rec(head, [n+1], head)
        return head