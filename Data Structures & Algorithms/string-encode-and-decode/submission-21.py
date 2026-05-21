class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []

        for s in strs:
            s = s.replace('(', '((')
            encoded.append(s)

        return str(len(strs)) + "|" + '('.join(encoded)
            

    def decode(self, s: str) -> List[str]:
        count_str, s = s.split("|", 1)
        if count_str == '0': return []

        ans = []
        oneAns = []
        slashFound = False
        for i in range(len(s)):
            if s[i] == '(' and (i == len(s)-1 or s[i+1] != '('):
                if slashFound:
                    slashFound = False
                    continue
                sOneAns = ''.join(oneAns) 
                ans.append(sOneAns)
                oneAns = []
            elif s[i] == '(':
                oneAns.append(s[i])
                slashFound = True
            else:
                oneAns.append(s[i])
        sOneAns = ''.join(oneAns) 
        ans.append(sOneAns)            
        return ans
