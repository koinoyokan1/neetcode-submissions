class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        print(people)
        l, r = 0, len(people)-1
        cnt = 0
        while l <= r:
            if l == r:
                cnt += 1
                break
            elif people[l] + people[r] <= limit:
                print(people[l], people[r])
                l += 1
                r -= 1
            else:
                print(people[r])
                r -= 1
            cnt += 1
        
        return cnt

