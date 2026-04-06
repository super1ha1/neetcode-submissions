# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        while head and cur: 
            head = head.next
            cur = cur.next
            if cur:
                cur = cur.next
            else:
                return False
            
            if head == cur:
                return True
        
        return False