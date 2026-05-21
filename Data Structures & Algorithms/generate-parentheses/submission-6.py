class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def _hlp(currAns=[], diff=0):
            if len(currAns) == 2*n:
                if diff == 0: return [''.join(currAns)]
                return []
            
            ans = []

            ans.extend(_hlp(currAns + ['('], diff+1))
            if diff > 0:
                ans.extend(_hlp(currAns + [')'], diff-1))

            return ans
        
        return _hlp()
