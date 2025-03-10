class Solution:
    def validate(self, node, minV, maxV):
        if node is None:
            return True

        if node.val <= minV or node.val >= maxV:
            return False

        return self.validate(node.left, minV, node.val) and self.validate(node.right, node.val, maxV)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, float('-inf'), float('inf'))