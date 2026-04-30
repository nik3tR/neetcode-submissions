# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        node = []
        curr = head
        while curr:
            node.append(curr)
            curr = curr.next
        
        first, last = 0, len(node) - 1

        while first < last:
            node[first].next = node[last]
            first += 1
            node[last].next = node[first]
            last -= 1
        
        node[first].next = None



        