class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = [len(temperatures)-1]

        for i in range(len(temperatures)-2, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()

            if stack:
                ans[i] = stack[-1] - i

            stack.append(i)

        return ans                