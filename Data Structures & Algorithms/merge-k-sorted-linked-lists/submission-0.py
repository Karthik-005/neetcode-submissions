# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, l1, l2) :
        dummy = ListNode(0, None)
        tail = dummy

        while l1 and l2 :
            if l1.val <= l2.val :
                tail.next = l1
                l1 = l1.next
                tail = tail.next

            else :
                tail.next = l2
                l2 = l2.next
                tail = tail.next

        if l1 :
            tail.next = l1
        elif l2 :
            tail.next = l2

        return dummy.next    

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 1 :
            return lists[0]
        if n == 0 :
            return None    

        l1 = self.mergeKLists(lists[0:n//2])
        l2 = self.mergeKLists(lists[n//2:])

        head = self.merge(l1, l2)

        return head