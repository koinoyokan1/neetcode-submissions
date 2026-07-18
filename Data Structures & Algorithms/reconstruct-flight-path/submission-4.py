class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        graph = defaultdict(list)

        for frm, to in tickets:
            graph[frm].append(to)

        ans = ["JFK"]
        flightsTaken = 0

        def dfs(frm):
            nonlocal flightsTaken

            if flightsTaken == len(tickets):
                return True

            for i in range(len(graph[frm])):
                to = graph[frm].pop(i)
                flightsTaken += 1
                ans.append(to)

                if dfs(to):
                    return True

                ans.pop()
                flightsTaken -= 1
                graph[frm].insert(i, to)

            return False

        dfs("JFK")
        return ans