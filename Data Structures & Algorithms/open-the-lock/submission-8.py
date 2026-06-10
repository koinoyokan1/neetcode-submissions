class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends: return -1
        cnt = 0
        start = (0,0,0,0)
        queue = deque([(cnt, start)])
        visited = {start}
        while queue:
            cnt, lock = queue.popleft()
            if ''.join(map(str, lock)) == target: return cnt 
            lock = list(lock)
            for i in range(4):
                for j in [-1, +1]:
                    lock[i] = (lock[i] + j) % 10
                    if ''.join(map(str, lock)) in deadends or tuple(lock) in visited: 
                        lock[i] = (lock[i] - j) % 10
                        continue 
                    visited.add(tuple(lock))
                    queue.append((cnt+1, tuple(lock)))
                    lock[i] = (lock[i] - j) % 10
        
        return -1