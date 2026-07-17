class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordListSet = set(wordList)
        wordListSet.add(beginWord)

        wordList = list(wordListSet)
        
        graph = defaultdict(list)

        def diffByOne(w1, w2):
            diffCnt = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]: 
                    diffCnt += 1
                    if diffCnt > 1: return False
            return diffCnt == 1

        def bfs(start, end):
            queue = deque([(start, 1)])
            visiting = set()

            while queue:
                n, cnt = queue.popleft()
                if n == end: return cnt
                for nei in graph[n]:
                    if nei in visiting: continue
                    visiting.add(nei)

                    queue.append((nei, cnt+1)) 

            return 0


        for i in range(len(wordList)):
            for j in range(i+1, len(wordList)):
                if diffByOne(wordList[i], wordList[j]):
                    graph[wordList[i]].append(wordList[j])
                    graph[wordList[j]].append(wordList[i])

        return bfs(beginWord, endWord)