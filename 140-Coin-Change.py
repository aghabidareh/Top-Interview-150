class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        A = [float('inf')] * (amount + 1)
        A[0] = 0
        coins = list(set(coins))

        for n in range(1, amount + 1):
            A_prev = [A[n - c] for c in coins if n - c >= 0]
            A[n] = 1 + min(A_prev) if A_prev else float('inf')

        return A[amount] if A[amount] != float('inf') else -1