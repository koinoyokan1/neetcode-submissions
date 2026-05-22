class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPal(s):
            return s == s[::-1]

        def _partition(i=0, b=[]):
            ans = b.copy()
            if i == len(s): 
                if isPal(ans[-1]):
                    return [ans]
                return []
            a = []
            if not ans:
                a.extend(_partition(i+1, [s[i]]))
            else:
                ans[-1] += s[i]
                a.extend(_partition(i+1, ans))
                ans[-1] = ans[-1][:-1]
                if isPal(ans[-1]): 
                    ans.append(s[i])
                    a.extend(_partition(i+1, ans))
                    ans = ans[:-1]
            return a
        
        return _partition()
