class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        for per in permutations(nums,len(nums)):
            result.append(list(per))
        return result