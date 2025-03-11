class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sorted_list = []
        while(head):
            sorted_list.append(head.val)
            head = head.next
        sorted_list.sort()
        sortedListNode = ListNode(0)
        head = sortedListNode
        for i in sorted_list:
            sortedListNode.next = ListNode(i)
            sortedListNode = sortedListNode.next
        return head.next