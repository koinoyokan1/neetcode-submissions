class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addNeighbor(self, n1, n2):
        self.graph[n1].append(n2)
        self.graph[n2].append(n1)

    def bfsSearch(self, n1, n2):
        steps = 1
        visited = set()
        queue = deque([(n1, steps)])

        while queue:
            node, steps = queue.popleft()
            print('Trying: ', node, steps)
            if node == n2: return steps

            for nei in self.graph[node]:
                if nei in visited: continue
                visited.add(nei)
                queue.append((nei, steps+1))
        
        return 0


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def validTransformation(w1, w2):
            if len(w1) != len(w2): return False
            err = 0
            for i in range(len(w1)):
                if w1[i] == w2[i]: continue
                err += 1
            return err <= 1
        
        graph = Graph()
        wordList = set(wordList)

        for word1 in wordList:
            for word2 in wordList:
                if validTransformation(word1, word2):
                    graph.addNeighbor(word1, word2)
        
        for word1 in wordList:
            if validTransformation(word1, beginWord):
                    graph.addNeighbor(word1, beginWord)
                                       

        return graph.bfsSearch(beginWord, endWord)
