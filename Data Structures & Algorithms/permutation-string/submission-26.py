'''

'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def isAnagram(s1, s2):
            return sorted(s1) == sorted(s2)
        left, right = 0, len(s1) - 1
        for right in range(left + len(s1) - 1, len(s2)):
            if isAnagram(s1, s2[left:right+1]): return True
            left += 1
        
        return False



