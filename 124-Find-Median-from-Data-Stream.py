
class MedianFinder:
    import heapq
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if len(self.max_heap) == 0 or -self.max_heap[0] > num:
            heapq.heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)

        if len(self.max_heap) > len(self.min_heap) + 1:
            swap = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, swap)
        elif len(self.min_heap) > len(self.max_heap):
            swap = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -swap)

    def findMedian(self) -> float:
        total_elements = len(self.max_heap) + len(self.min_heap)

        if total_elements % 2 == 0:
            root = -self.max_heap[0]
            leaf = self.min_heap[0]
            median = (root + leaf) / 2
        else:
            median = -self.max_heap[0]
        return median