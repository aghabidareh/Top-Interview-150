class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        rightmost_nodes = {}
        q = deque([(root, 0)])

        while q:
            node, depth = q.popleft()

            if depth not in rightmost_nodes:
                rightmost_nodes[depth] = node.val

            if node.right:
                q.append((node.right, depth + 1))
            if node.left:
                q.append((node.left, depth + 1))

        return list(rightmost_nodes.values())