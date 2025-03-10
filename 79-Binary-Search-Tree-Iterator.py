class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        top_node = self.stack.pop()

        if top_node.right:
            self._leftmost_inorder(top_node.right)

        return top_node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0