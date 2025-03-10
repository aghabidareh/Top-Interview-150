class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        q = deque()
        q.append(root)
        dummy = Node(-999)
        while q:
            length = len(q)

            prev = dummy
            for _ in range(length):
                popped = q.popleft()
                if popped.left:
                    q.append(popped.left)
                    prev.next = popped.left
                    prev = prev.next
                if popped.right:
                    q.append(popped.right)
                    prev.next = popped.right
                    prev = prev.next

        return root