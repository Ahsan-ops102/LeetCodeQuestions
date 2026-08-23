# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA = headA
        pB = headB
        switchedA = False
        switchedB = False

        while pA != pB:
            pA = pA.next
            pB = pB.next

            if pA == None and switchedA == False: 
                pA = headB
                switchedA = True
            if pB == None and switchedB == False:
                pB = headA
                switchedB = True
           
            
            
        return pA
        
