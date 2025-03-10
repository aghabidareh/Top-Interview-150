class Solution:
    def __init__(self):
        self.min_diff = 100001
        self.last_val = None

    def _inorder_traversal(self, root):
        if not root:
            return

        if root.left:
            self._inorder_traversal(root.left)

        if self.last_val is not None:
            self.min_diff = min(self.min_diff, abs(root.val - self.last_val))
            self.last_val = root.val
        else:
            self.last_val = root.val

        if root.right:
            self._inorder_traversal(root.right)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self._inorder_traversal(root)
        return self.min_diff