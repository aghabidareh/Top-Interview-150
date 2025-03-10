class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float('-inf')

        def dfs(node):
            if node == None:
                return 0

            leftMax = max(dfs(node.left), 0)
            rightMax = max(dfs(node.right), 0)

            currentPathSum = node.val + leftMax + rightMax

            self.maxSum = max(self.maxSum, currentPathSum)

            return node.val + max(leftMax, rightMax)

        dfs(root)
        return self.maxSum   