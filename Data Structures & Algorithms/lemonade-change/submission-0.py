class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = defaultdict(int)

        for b in bills:
            give = b - 5
            if give == 0:
                change[5] += 1
                continue
            if give == 5:
                change[10] += 1
                if change[5] == 0: return False
                change[5] -= 1
                continue
            if give == 15:
                change[20] += 1
                if change[10] > 0 and change[5] > 0:
                    change[10] -= 1
                    change[5] -= 1
                    continue
                if change[5] >= 3:
                    change[5] -= 3
                    continue
                return False

            return False
        return True