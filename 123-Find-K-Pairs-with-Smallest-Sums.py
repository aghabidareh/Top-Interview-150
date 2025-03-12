class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        hq = []
        output = []
        for i in range(min(len(nums1), k)):
            heapq.heappush(hq, (nums1[i]+nums2[0], [nums1[i], nums2[0]], 0))
        while k > 0 and hq:
            x, ele, idx = heapq.heappop(hq)
            output.append(ele)
            if idx + 1 < len(nums2):
                heapq.heappush(hq, (ele[0]+nums2[idx+1],[ele[0], nums2[idx+1]], idx+1))
            k -= 1
        return output