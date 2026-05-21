class Solution:
    def _checkInclusion(self, s1, s2, _s1Counter, s2i):
        s1Counter = _s1Counter.copy()
        
        for i in range(s2i, len(s1) + s2i):
            if s1Counter[s2[i]] > 0: s1Counter[s2[i]] -= 1
            else: return False

        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Counter = Counter(s1)

        for i in range(len(s2) - len(s1) + 1):
            if s1Counter[s2[i]] == 0: continue
            if self._checkInclusion(s1, s2, s1Counter, i): return True

        return False