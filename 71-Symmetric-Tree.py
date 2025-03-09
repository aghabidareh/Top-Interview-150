class Solution(object):
    def isSymmetric(self, root):
        q=deque()
        q.append(root.left)
        q.append(root.right)
        while q:
            l=q.popleft()
            r=q.popleft()
            if not l and not r:
                continue
            if not l or not r:
                return False
            if l.val!=r.val:
                return False
            q.append(l.left)
            q.append(r.right)
            q.append(l.right)
            q.append(r.left)
        return True