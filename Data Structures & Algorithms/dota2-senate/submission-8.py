class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        d, r = deque(), deque()

        for i in range(len(senate)):
            s = senate[i]
            if s == 'D': d.append(i)
            else: r.append(i)
        
        while d and r:
            prev = max(d[-1], r[-1]) + 1
            if d[0] > r[0]:
                _ = d.popleft()
                v = r.popleft()
                r.append(v + prev)
            else:
                v = d.popleft()
                _ = r.popleft()
                d.append(v + prev)

        if d: return 'Dire'
        return 'Radiant'