class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        current=n
        for i in range(n):
            matrix.append([])
        for r in range(n):
            for c in range(n):
                matrix[current].insert(0,matrix[r][c])
                current+=1
            current=n
        for j in range(n):
            matrix.pop(0)