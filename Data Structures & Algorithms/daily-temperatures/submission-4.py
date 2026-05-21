class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 0: return []

        ans = [0] * len(temperatures)
        stack = [len(temperatures)-1]

        for i in range(len(temperatures)-1, -1, -1):
            t = temperatures[i]
            while stack and t >= temperatures[stack[-1]]:
                stack.pop()
            if stack: ans[i] = stack[-1] - i
            stack.append(i)
            print(stack)
        return ans

