class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            return root.val == targetSum

        targetSum = targetSum - root.val
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)