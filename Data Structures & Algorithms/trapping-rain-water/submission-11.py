class Solution:
    def trap(self, height: List[int]) -> int:
        prefixTallest, suffixTallest = [0] * len(height), [0] * len(height)

        for i in range(1, len(height)):
            prefixTallest[i] = max(height[i-1], prefixTallest[i-1])
        
        for i in range(len(height)-2, -1, -1):
            suffixTallest[i] = max(suffixTallest[i+1], height[i+1])

        water = 0
        for i in range(len(height)):
            water += max(min(suffixTallest[i], prefixTallest[i]) - height[i], 0)

        return water