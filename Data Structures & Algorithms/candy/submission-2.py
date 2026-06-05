from functools import lru_cache

class Solution:
    def candy(self, ratings: List[int]) -> int:
        visited = set()

        @lru_cache(maxsize=None)
        def assignCandies(i):
            ans = 1
            if i < len(ratings) - 1  and ratings[i] > ratings[i+1]:
                ans = assignCandies(i+1) + 1
            if i > 0 and ratings[i] > ratings[i-1]:
                ans = max(ans, assignCandies(i-1) + 1)
            return ans

        candies = 0
        for i in range(len(ratings)):
            candies += assignCandies(i)
        
        return candies
