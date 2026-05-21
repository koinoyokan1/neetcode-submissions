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

        def _letterCombinations(i=0, currComb=""):
            if i == len(digits): return [currComb]

            chars = self.digitToChar[digits[i]]

            ans = []
            for c in chars:
                ans.extend(_letterCombinations(i+1, currComb + c))
            
            return ans
        return _letterCombinations()