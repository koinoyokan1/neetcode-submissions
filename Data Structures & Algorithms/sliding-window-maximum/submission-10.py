import heapq
# 1 2 1 0 4 2 6
# 
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k >= len(nums): return [max(nums)]

        monoDecrQueue = deque([])

        def validWindow(left, right):
            return right - left + 1 == k

        def addToMonoDecrQueue(index):
            while monoDecrQueue and nums[monoDecrQueue[-1]] <= nums[index]:
                monoDecrQueue.pop()
            monoDecrQueue.append(index)
            
        def getFromMonoDecrQueue(index):
            while monoDecrQueue and monoDecrQueue[0] < index:
                monoDecrQueue.popleft()
            return monoDecrQueue[0]

        ans = []
        left = 0

        for right in range(len(nums)):
            addToMonoDecrQueue(right)
            if validWindow(left, right):
                ans.append(nums[getFromMonoDecrQueue(left)])
                left += 1

        return ans

        
