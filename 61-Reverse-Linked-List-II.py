class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        left_i, right_i = left, right
        sentinel = ListNode(next=head)

        before_left, left = sentinel, sentinel.next
        for _ in range(left_i - 1):
            before_left, left = left, left.next

        right, after_right = left, left.next
        before_right = None
        for _ in range(right_i - left_i):
            before_right, right.next, right, after_right = right, before_right, after_right, after_right.next
        right.next = before_right
        before_left.next = right
        left.next = after_right
        return sentinel.next