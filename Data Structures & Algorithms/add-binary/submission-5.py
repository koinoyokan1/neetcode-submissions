class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = []

        if len(b) > len(a): a, b = b, a
        b = "0"*(len(a)-len(b)) + b
        c = 0
        for i in range(len(b)-1, -1, -1):
            curr = int(b[i]) + int(a[i]) + c
            if curr == 3:
                ans.append('1')
                c = 1
                continue
            if curr == 2:
                ans.append('0')
                c = 1
                continue
            if curr == 1:
                ans.append('1')
                c = 0
                continue
            if curr == 0:
                ans.append('0')
        if c == 1: ans.append('1')
        return ''.join(ans[::-1])    
        
