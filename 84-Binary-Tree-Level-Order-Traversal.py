class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        import queue
        result = []
        if root is None:
            return result

        q = queue.Queue()
        q.put(root)

        while not q.empty():
            c_size = q.qsize()
            c_level = []

            for _ in range(c_size):
                c_node = q.get()
                c_level.append(c_node.val)

                if c_node.left:
                    q.put(c_node.left)

                if c_node.right:
                    q.put(c_node.right)

            result.append(c_level)
        return result