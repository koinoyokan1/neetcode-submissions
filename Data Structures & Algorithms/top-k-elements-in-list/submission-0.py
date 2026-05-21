class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []

        cntr = Counter(nums)

        for num in cntr.keys():
            cnt = cntr[num]
            heapq.heappush(heap, (cnt, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for _, num in heap]