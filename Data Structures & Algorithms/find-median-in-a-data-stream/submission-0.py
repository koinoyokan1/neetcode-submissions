class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        l1 = len(self.maxHeap)
        l2 = len(self.minHeap)

        if len(self.maxHeap) == 0: 
            heapq.heappush(self.maxHeap, -num)
            return
            
        leftMedian = self.maxHeap[0]
        
        if num <= -leftMedian:
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
        