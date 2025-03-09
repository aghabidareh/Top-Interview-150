class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            invert = self.invertTree
            root.left, root.right = invert(root.right), invert(root.left)
            return root