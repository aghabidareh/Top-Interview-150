class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def createPattern(s: str, l: int, r: int) -> str:
            if l == r and len(s) == 2 * n:
                answer.append(s)
                return
            if (r < l):
                createPattern(s + ")", l, r + 1)
            if (l < n):
                createPattern(s + "(", l + 1, r)

        answer = []
        createPattern("", 0, 0)

        return answer