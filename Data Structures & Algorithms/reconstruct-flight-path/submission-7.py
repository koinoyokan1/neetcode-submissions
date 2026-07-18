class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        graph = defaultdict(list)

        for frm, to in tickets:
            graph[frm].append(to)
        
        ans = ["JFK"]

        def dfs(frm):
            if len(ans) == len(tickets) + 1:
                return True

            for i in range(len(graph[frm])):
                to = graph[frm][i]
                graph[frm].pop(i)
                ans.append(to)

                if dfs(to):
                    return True

                ans.pop()
                graph[frm].insert(i, to)

            return False

        dfs("JFK")
        return ans
