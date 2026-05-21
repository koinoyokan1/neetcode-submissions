class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        s1Cnt = Counter(s1)

        for right in range(len(s2)):
            s1Cnt[s2[right]] -= 1

            while s1Cnt[s2[right]] == -1:

                s1Cnt[s2[left]] += 1
                left += 1

            if right - left + 1 == len(s1): 
                return True
        
        return False