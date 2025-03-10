class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = [(root,1)]
        result = []
        curr = 0
        flag = 1
        while(queue):
            node, level = queue.pop(0)
            if(level > curr):
                flag = -1*flag
            if(flag == -1):
                if(level > curr):
                    result.append([node.val])
                    curr += 1
                else:
                    result[-1].append(node.val)
            elif(flag == 1):
                if(level > curr):
                    result.append([node.val])
                    curr += 1
                else:
                    result[-1].insert(0,node.val)
            if(node.left):
                queue.append((node.left, level + 1))
            if(node.right):
                queue.append((node.right, level + 1))
        return result