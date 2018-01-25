# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        leftTemp = 0
        
        output = []
        
        while ((l1 != None) or (l2 != None)):
            #get left value and set next node
            if l1:
                leftTemp = l1.val
                l1 = l1.next
            else:
                leftTemp = 0
            #get right value     and set next node
            if l2:
                rightTemp = l2.val
                l2 = l2.next
            else:
                rightTemp = 0
                
            totalTemp = leftTemp + rightTemp
            #add carry
            totalTemp += carry
            #reset carry
            carry = totalTemp / 10
            #add to the output
            output.append(totalTemp % 10)
            
        
        if carry == 1:
            output.append(1)
        
        return output
