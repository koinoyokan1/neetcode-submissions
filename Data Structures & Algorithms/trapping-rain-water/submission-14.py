class Solution:
    def fillMaxToLeft(self, arr, maxToLeft):
        maxToLeft[0] = 0
        for i in range(1, len(arr)):
            maxToLeft[i] = max(maxToLeft[i-1], arr[i-1])

    def trap(self, height: List[int]) -> int:
        maxToLeft = [0 for _ in range(len(height))]
        maxToRight = [0 for _ in range(len(height))]

        self.fillMaxToLeft(height, maxToLeft)
        self.fillMaxToLeft(height[::-1], maxToRight)
        maxToRight = maxToRight[::-1]

        areaWater = 0
        for i in range(len(height)):
            tmp = min(maxToLeft[i], maxToRight[i]) - height[i]
            currWater = max(tmp, 0)
            areaWater += currWater

        return areaWater
