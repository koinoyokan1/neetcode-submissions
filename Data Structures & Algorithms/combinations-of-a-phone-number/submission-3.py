class Solution:
    def __init__(self):
        self.digitToChar = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "qprs",
        "8": "tuv",
        "9": "wxyz",
        }

    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "": return []

        def _lc(i=0, curr=""):
            if i == len(digits): return [curr]
            ans = []
            for opt in self.digitToChar[digits[i]]:
                ans.extend(_lc(i+1, curr + opt))
            return ans

        return _lc()            
        
