class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cntr = defaultdict(list)

        for s in strs:
            ss = str(sorted(s))
            cntr[ss].append(s)
        
        return list(cntr.values())