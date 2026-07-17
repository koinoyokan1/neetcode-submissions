class TrieNode:
    def __init__(self):
        self.isEOW = False
        self.word = ""
        self.children = [None] * 26

class Solution:
    def fillWordToTrie(self, node, word, wordi=0):
        if wordi == len(word): 
            node.isEOW = True
            node.word = word
            return

        index = ord(word[wordi]) - ord('a')

        if not node.children[index]: node.children[index] = TrieNode()
        node = node.children[index]

        self.fillWordToTrie(node, word, wordi+1)

    def fillWordsToTrie(self, root, words):
        for w in words:
            self.fillWordToTrie(root, w)

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        self.fillWordsToTrie(root, words)
        
        visiting = set()

        ans = set()
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def recFindWord(node, i, j):
            if node.isEOW: ans.add(node.word)

            for di, dj in dirs:
                ni, nj = i + di, j + dj

                if (
                    0 <= ni < len(board)
                    and 0 <= nj < len(board[0])
                    and node.children[ord(board[ni][nj]) - ord('a')] 
                    and (ni, nj) not in visiting
                ):
                    visiting.add((ni, nj))
                    recFindWord(node.children[ord(board[ni][nj]) - ord('a')], ni, nj)
                    visiting.remove((ni, nj))

        def dfs():
            visiting.clear()

            for i in range(len(board)):
                for j in range(len(board[0])):
                    index = ord(board[i][j]) - ord('a')
                    if root.children[index]:
                        visiting.add((i, j))
                        recFindWord(root.children[index], i, j)
                        visiting.remove((i, j))
        dfs()
        return list(ans)