class Solution:
    def trap(self, height: List[int]) -> int:
        prefixTallest, suffixTallest = [0] * len(height), [0] * len(height)

        tallest = 0
        for i in range(1, len(height)):
            prefixTallest[i] = max(height[i-1], tallest)
            tallest = prefixTallest[i]
        
        print(prefixTallest)
        tallest = 0
        for i in range(len(height)-2, -1, -1):
            suffixTallest[i] = max(tallest, height[i+1])
            tallest = suffixTallest[i]
        print(suffixTallest)
        water = 0
        for i in range(len(height)):
            water += max(min(suffixTallest[i], prefixTallest[i]) - height[i], 0)

        return water