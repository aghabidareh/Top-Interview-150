class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        return left & (-1 << (left ^ right).bit_length())