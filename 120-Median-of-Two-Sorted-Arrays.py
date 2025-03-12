class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = nums1 + nums2
        num.sort()
        n = len(num)
        if n % 2 == 1:
            return float(num[n // 2])
        else:
            m1 = num[(n // 2) - 1]
            m2 = num[n // 2]
            return (float(m1) + float(m2)) / 2.0
