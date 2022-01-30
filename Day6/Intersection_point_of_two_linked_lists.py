# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        dummy1 = headA
        dummy2 = headB
        
        while dummy1!=dummy2:
            if dummy1==None:
                dummy1 = headB
            else:
                dummy1 = dummy1.next
            if dummy2==None:
                dummy2 = headA
            else:
                dummy2 = dummy2.next
        return dummy1
                
        
