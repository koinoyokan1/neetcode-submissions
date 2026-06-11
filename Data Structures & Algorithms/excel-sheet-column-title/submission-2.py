# 53 2A
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        c = columnNumber 
        ans = ""
        while c:
            c -= 1
            ans = chr(c % 26 + ord('A')) + ans
            c = c // 26
        
        return ans