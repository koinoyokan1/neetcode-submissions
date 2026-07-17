class TrieNode:
    def __init__(self):
        self.eow = False
        self.word = ""
        self.children = [None] * 26


class Solution:
    def addToTrie(self, node, w, i=0):
        if i == len(w):
            node.eow = True
            node.word = w
            return

        idx = ord(w[i]) - ord('a')

        if not node.children[idx]:
            node.children[idx] = TrieNode()

        self.addToTrie(node.children[idx], w, i + 1)


    def validSentence(self, s, root, node, i, path, ans):
        # reached end of string
        if i == len(s):
            if node.eow:
                ans.append(" ".join(path + [node.word]))
            return

        # if current prefix is a word, restart from root
        if node.eow:
            self.validSentence(
                s,
                root,
                root,
                i,
                path + [node.word],
                ans
            )

        idx = ord(s[i]) - ord('a')

        if node.children[idx]:
            self.validSentence(
                s,
                root,
                node.children[idx],
                i + 1,
                path,
                ans
            )


    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        root = TrieNode()

        for w in wordDict:
            self.addToTrie(root, w)

        ans = []
        self.validSentence(s, root, root, 0, [], ans)

        return ans