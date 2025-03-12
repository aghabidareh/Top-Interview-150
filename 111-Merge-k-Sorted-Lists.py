# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) < 1:
            return None
        head_node = ListNode(0)
        head_node.next = lists[0]
        for i in range(1,len(lists)):
            first_node = head_node
            temp = lists[i]
            while first_node.next != None and temp != None:
                if first_node.next.val > temp.val:
                    new_node = ListNode(temp.val)
                    new_node.next = first_node.next
                    first_node.next = new_node
                    temp = temp.next
                first_node = first_node.next
            while first_node.next != None:
                first_node = first_node.next
            first_node.next = temp

        return head_node.next