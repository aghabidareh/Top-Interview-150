class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        i = head
        j = head
        while j and j.next and j.next.next:
           i = i.next
           j = j.next.next
           if i == j:
               return True
        return False