class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def _partition(i=0, currAns=[]):
            def isPal(s):

                l, r = 0, len(s) - 1
                while l <= r:
                    if s[l] != s[r]: 
                        return False
                    l += 1
                    r -= 1

                return True

            if i == len(s): 
                return [currAns]

            ans = []
            for j in range(i, len(s)):
                if isPal(s[i:j+1]):
                    ans.extend(_partition(j+1, currAns + [s[i:j+1]]))
            return ans

        return _partition()