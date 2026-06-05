from functools import lru_cache

class Solution:
    def candy(self, ratings: List[int]) -> int:

        @lru_cache(None)
        def assignCandies(i):
            ans = 1

            if i > 0 and ratings[i] > ratings[i - 1]:
                ans = assignCandies(i - 1) + 1

            if i < len(ratings) - 1 and ratings[i] > ratings[i + 1]:
                ans = max(ans, assignCandies(i + 1) + 1)

            return ans

        return sum(assignCandies(i) for i in range(len(ratings)))