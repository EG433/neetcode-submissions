# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        prev, curr = None, head
        count = set()
        while curr:
            if curr not in count:
                count.add(curr)
                temp = curr.next
                prev = curr
                curr = temp
            else:
                return True
        return False
        