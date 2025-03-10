class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node

        q, clones = deque([node]), {node.val: Node(node.val, [])}
        while q:
            current = q.popleft()
            current_clone = clones[current.val]

            for ngbr in current.neighbors:
                if ngbr.val not in clones:
                    clones[ngbr.val] = Node(ngbr.val, [])
                    q.append(ngbr)

                current_clone.neighbors.append(clones[ngbr.val])

        return clones[node.val]