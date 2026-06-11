from functools import lru_cache

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @lru_cache(maxsize=None)
        def game(i=0, m=1, aliceTurn=True):
            if i >= len(piles): 
                return 0

            maxX = 2*m

            if aliceTurn:
                maxStones = -1

                for x in range(maxX):
                    if i + x == len(piles): break

                    maxStones = max(maxStones, game(i+x+1, max(x+1, m), not aliceTurn) + sum(piles[i:i+x+1]))
                return maxStones
            else:
                minStones = math.inf
                for x in range(maxX):
                    if i + x == len(piles): break
                    minStones = min(minStones, game(i+x+1, max(x+1, m), not aliceTurn))
                return minStones

        return game()
