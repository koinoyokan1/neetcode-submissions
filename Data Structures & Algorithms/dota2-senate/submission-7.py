class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        d, r = deque(), deque()
        for i in range(len(senate)):
            s = senate[i]
            if s == 'D':
                d.append(i)
            else:
                r.append(i)
        
        dl = 0
        while d and r:
            if d[0] > r[0]:
                prev = max(d[-1], r[-1]) + 1
                _ = d.popleft()
                v = r.popleft()
                r.append(v + prev)
            else:
                prev = max(d[-1], r[-1]) + 1
                v = d.popleft()
                _ = r.popleft()
                d.append(v + prev)
            dl += 1
        if d: return 'Dire'
        return 'Radiant'