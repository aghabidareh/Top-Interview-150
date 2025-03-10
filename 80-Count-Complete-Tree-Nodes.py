class Solution:
    def findDepth(self, root) -> int:
        if not root:
            return 0
        return 1 + self.findDepth(root.left)

    def check(self, root, path) -> bool:
        for i in path:
            if i == 0:
                root = root.left
            else:
                root = root.right

        if root:
            return True
        else:
            return False

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth = self.findDepth(root)

        path = [0 for _ in range(depth - 1)]

        for i in range(len(path)):
            path[i] = 1
            present = self.check(root, path)
            if not present:
                path[i] = 0

        count = 2 ** (depth - 1) - 1

        for i, x in enumerate(path[::-1]):
            count += x * 2 ** i

        count += 1

        return count