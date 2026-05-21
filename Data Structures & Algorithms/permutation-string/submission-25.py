'''

'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left, right = 0, len(s1) - 1
        s1 = list(s1)
        s1.sort()
        subStr = ""
        for right in range(left + len(s1) - 1, len(s2)):
            subStr = list(s2[left:right+1])
            subStr.sort()
            if subStr == s1: return True
            left += 1
        
        return False



