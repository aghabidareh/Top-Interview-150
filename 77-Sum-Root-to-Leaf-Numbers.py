class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(current,num):
            if current is None:
                return 0
            num=num*10+current.val
            if not current.left  and not current.right:
                return num
            return dfs(current.left,num)+dfs(current.right,num)
        return dfs(root,0)