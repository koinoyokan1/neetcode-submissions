class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        s1Cnt = Counter(s1)

        def invalidWindow():
            any(s2CurrSet) not in s1Cnt.values()

        for right in range(len(s2)):
            s1Cnt[s2[right]] -= 1

            while -1 in list(s1Cnt.values()):

                s1Cnt[s2[left]] += 1
                left += 1

            if right - left + 1 == len(s1): 
                return True
        
        return False