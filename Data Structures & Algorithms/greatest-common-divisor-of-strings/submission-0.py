class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2): 
            str1, str2 = str2, str1
        
        l1 = len(str1)
        l2 = len(str2)

        for i in range(l2-1, -1, -1):
            if l1 % (i+1) != 0 or l2 % (i+1) != 0: continue
            reps1 = l1 // (i+1)
            reps2 = l2 // (i+1)
            if reps1 * str2[:i+1] == str1 and reps2 * str2[:i+1] == str2:
                return str2[:i+1]
        return ""