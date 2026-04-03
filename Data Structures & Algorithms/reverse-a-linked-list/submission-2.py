# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# None 0 -> 1 -> 2 -> 3

# prev = None
# cur = 0
# next = 1

# prev = 0
# cur = 1
# next = 2

# prev = 1
# cur = 2
# next = 3

# prev = 2
# cur = 3
# next = None

# prev = 3
# cur = None
# next = None



class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        next = None
        if cur:
            next = cur.next
        while cur:
            cur.next = prev
            prev = cur
            cur = next
            if cur:
                next = cur.next       
            else:
                next = None

        return prev
            