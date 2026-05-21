class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []

        cntr = Counter(nums)

        for num in cntr.keys():
            heapq.heappush(heap, (cntr[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [i[1] for i in heap]