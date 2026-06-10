class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ordMap = {}
        for i in range(len(order)):
            ordMap[order[i]] = i

        for i in range(1, len(words)):
            w1 = words[i-1]
            w2 = words[i]

            for j in range(min(len(w1), len(w2))):
                c1, c2 = w1[j], w2[j]

                if c1 == c2: continue
                if ordMap[c1] > ordMap[c2]: 
                    
                    return False
                break
            else:
                if len(w1) > len(w2): return False
        
        return True

