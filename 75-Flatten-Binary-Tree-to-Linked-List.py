class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        current=root
        while current:
            if current.left!=None:
                prev=current.left
                while prev.right:
                    prev=prev.right
                prev.right=current.right
                current.right=current.left
                current.left=None
            current=current.right