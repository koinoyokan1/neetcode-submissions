from functools import lru_cache
class TNode:
    def __init__(self):
        self.isEOW = False
        self.children = [None for i in range(26)]

class Solution:
    def addToTrie(self, head, w):
        p = head
        for c in w:
            c = ord(c) - ord('a')
            if not p.children[c]: p.children[c] = TNode()
            p = p.children[c]
        p.isEOW = True

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        head = TNode()

        for w in dictionary:
            self.addToTrie(head, w)
        
        @lru_cache
        def findS(i=0, p=head):
            if i == len(s):
                return 0 if (p == head or p.isEOW) else math.inf
            ans = math.inf
            if p == head:
                ans = min(ans, findS(i+1, head) + 1)
            c = ord(s[i]) - ord('a')
            if p.children[c]:
                ans = min(ans, findS(i+1, p.children[c]))
            if p.children[c] and p.children[c].isEOW:
                ans = min(ans, findS(i+1, head))
            return ans

        return findS()
