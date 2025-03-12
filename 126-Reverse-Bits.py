class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result <<= 1
            bit = n & 1
            result = result | bit
            n >>= 1

        return result