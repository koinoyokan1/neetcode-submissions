class Node:
    def __init__(self):
        self.isEow = False
        self.children = [None] * 26

class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root

        for c in word:
            c = ord(c) - ord('a')
            if not node.children[c]: node.children[c] = Node()
            node = node.children[c]
        node.isEow = True

    def search(self, word: str) -> bool:
        def _search(i=0, startNode=self.root):
            if i == len(word): return startNode.isEow

            if word[i] == '.':
                for j in range(26):
                    if startNode.children[j] and _search(i+1, startNode.children[j]): return True
                return False

            m = ord(word[i]) - ord('a')
            if not startNode.children[m]: return False
            return _search(i+1, startNode.children[m])

        return _search()








