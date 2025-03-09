class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1
        current.next = head

        k = k % length
        target = length - k

        current = head
        count = 1
        while count < target:
            current = current.next
            count += 1

        new_head = current.next
        current.next = None

        return new_head