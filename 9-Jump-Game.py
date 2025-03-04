class Solution:
    def canJump(self, nums: List[int]) -> bool:
        g = 0
        for number in nums:
            if g < 0:
                return False
            elif number > g:
                g = number
            g -= 1

        return True