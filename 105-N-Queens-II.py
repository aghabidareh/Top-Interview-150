class Solution:
    def totalNQueens(self, n: int) -> int:
        colSet = set()
        negDia = set()
        posDia = set()
        result = 0

        def backtrack(i):
            nonlocal result
            if i == n:
                result += 1
                return
            for j in range(n):
                if j in colSet or (i - j) in negDia or (i + j) in posDia:
                    continue
                colSet.add(j)
                negDia.add(i - j)
                posDia.add(i + j)
                backtrack(i + 1)
                colSet.remove(j)
                negDia.remove(i - j)
                posDia.remove(i + j)

        backtrack(0)
        return result