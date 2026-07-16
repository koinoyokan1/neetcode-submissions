
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [-1] + heights + [-1]

        monoIncStack = [0]
        nextSmallerToLeft = [-1]
        for i in range(1, len(heights)-1):
            while heights[monoIncStack[-1]] >= heights[i]:
                  monoIncStack.pop()
            nextSmallerToLeft.append(monoIncStack[-1])

            monoIncStack.append(i)
        nextSmallerToLeft.append(-1)
        print(nextSmallerToLeft)

        monoIncStack = [len(heights)-1]
        nextSmallerToRight = [-1]
        for i in range(len(heights)-2, 0, -1):
            while heights[monoIncStack[-1]] >= heights[i]:
                  monoIncStack.pop()
            nextSmallerToRight.append(monoIncStack[-1])

            monoIncStack.append(i)
        nextSmallerToRight.append(-1)
        nextSmallerToRight = nextSmallerToRight[::-1]
        print(nextSmallerToRight)

        mx = 0
        for i in range(1, len(heights)-1):
            mx = max(mx, heights[i]*(nextSmallerToRight[i]-nextSmallerToLeft[i]-1))
        
        return mx
        

