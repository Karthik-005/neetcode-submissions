# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        def reverse(l1, l2):
            if not l1 and l2 :
                return l2

            elif l1 and not l2:
                return l1   

            elif not l1 and not l2:
                return None         

            
            if l1.val <= l2.val:
                head = l1
                l1 = l1.next

            else:
                head = l2
                l2 = l2.next
                    
            
            head.next = reverse(l1, l2)

            return head   

        return reverse(list1, list2)          