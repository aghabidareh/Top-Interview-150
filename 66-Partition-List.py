class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = ListNode()
        right = ListNode()
        lTrail = left
        rTrail = right
        while head:
            if head.val < x:
                lTrail.next = head
                lTrail = lTrail.next
            else:
                rTrail.next = head
                rTrail = rTrail.next
            head = head.next
        lTrail.next = right.next
        rTrail.next = None
        return left.next