class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        maxVol = 0

        while i < j:
            currVol = min(heights[i], heights[j]) * (j - i)
            maxVol = max(maxVol, currVol)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return maxVol