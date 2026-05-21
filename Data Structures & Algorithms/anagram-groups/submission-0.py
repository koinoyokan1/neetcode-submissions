class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}
        for s in strs:
            sList = list(s)
            sList.sort()
            sIndex = str(sList)
            if sIndex not in dct:
                dct[sIndex] = [s]
            else:
                dct[sIndex].append(s)
        
        ans = []
        for key in dct.keys():
            ans.append(dct[key])
        
        return ans