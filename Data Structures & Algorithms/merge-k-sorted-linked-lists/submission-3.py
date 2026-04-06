# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def printList(cur):
            res = []
            while cur:
                res.append(cur.val)
                cur = cur.next
            print(res)
            
        def merge2List(first, second):
            head = ListNode()
            cur = head
            while first and second:
                if first.val < second.val:
                    cur.next = first
                    first = first.next
                else:
                    cur.next = second
                    second = second.next
                cur = cur.next
            
            cur.next = first or second

            return head.next
        
        if len(lists) == 0:
            return None

        for i in range(1, len(lists)):
            print(f'to merge:')
            lists[i] = merge2List(lists[i], lists[i-1])
            print(f'after merge: ')
        
        return lists[-1]