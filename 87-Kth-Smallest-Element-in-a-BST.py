class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []

        def inOrder(root):
            if root == None:
                return

            inOrder(root.left)
            result.append(root.val)
            inOrder(root.right)

        inOrder(root)

        return result[k - 1]