"""
xyxxyzbzbbisl
     l
    r

x:[0,3]
y:[]
z:[]
b:[]

"""
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if len(s) == 0: return []

        rightmost = {}

        for i in range(len(s)):
            rightmost[s[i]] = i

        
        left, right = 0, 0
        ans = []

        while left < len(s):
            maxRight = rightmost[s[left]]
            while right < maxRight:
                maxRight = max(maxRight, rightmost[s[right]])
                right += 1
            ans.append(right - left + 1)
            left = right + 1

        return ans