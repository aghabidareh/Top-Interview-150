class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue: Deque[tuple[int, int]] = deque()
        queue.append((root, 0))

        map: DefaultDict[int, int] = defaultdict(list)

        while queue:
            node, position = queue.popleft()
            map[position].append(node.val)

            if node.left:
                queue.append((node.left, position + 1))
            if node.right:
                queue.append((node.right, position + 1))

        return [sum(nums) / len(nums) for nums in map.values()]