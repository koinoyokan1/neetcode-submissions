
import bisect

class TimeMap:
    def __init__(self):
        self.dct = defaultdict(list)
        self.value = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dct[key].append(timestamp)
        self.value[timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        candidates = self.dct[key]
        if len(candidates) == 0: return ""
        t = bisect.bisect_left(candidates, timestamp)
        if t == len(candidates): return self.value[candidates[-1]]
        if candidates[t] == timestamp: return self.value[timestamp]
        if t == 0: return ""
        return self.value[candidates[t-1]]
