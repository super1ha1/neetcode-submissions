# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        head = None
        tail = None
        while list1 and list2:
            if list1.val <= list2.val:
                # append list1
                if head:
                    tail.next = list1
                    tail = tail.next
                else:
                    # init
                    head = list1
                    tail = head   

                list1 = list1.next
                tail.next = None

            else:
                if head:
                    tail.next = list2
                    tail = tail.next
                else:
                    head = list2
                    tail = head
                list2 = list2.next
                tail.next = None
        
        if list1:
            tail.next = list1

        if list2:
            tail.next = list2

        return head