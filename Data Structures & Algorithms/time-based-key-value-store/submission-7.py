
import bisect

class TimeMap:
    def __init__(self):
        self.dct = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dct[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        candidates = self.dct[key]
        if len(candidates) == 0: return ""

        t = bisect.bisect_left(candidates, timestamp, key=lambda x:x[0])
        print(t)
        if t == len(candidates): return candidates[-1][1]

        if candidates[t][0] == timestamp: return candidates[t][1]
        if t == 0: return ""

        return candidates[t-1][1]
