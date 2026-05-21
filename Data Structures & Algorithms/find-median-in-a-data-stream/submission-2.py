class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if len(self.maxHeap) == 0 or num <= -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
            if len(self.maxHeap) > len(self.minHeap) + 1:
                val = -heapq.heappop(self.maxHeap) 
                heapq.heappush(self.minHeap, val)
        else:
            heapq.heappush(self.minHeap, num)
            if len(self.minHeap) > len(self.maxHeap):
                val = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, -val)

    def findMedian(self) -> float:
        if len(self.minHeap) > 0:
            print(self.minHeap[0])
        if len(self.maxHeap) > len(self.minHeap): return -self.maxHeap[0]
        return (-self.maxHeap[0] + self.minHeap[0])/2
        