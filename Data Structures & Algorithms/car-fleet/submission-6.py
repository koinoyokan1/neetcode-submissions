
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
            position = [[position[i], i] for i in range(len(position))]
            position.sort(reverse=True)

            cnt = 0
            prevTm = -1

            for p, i in position:
                spd = speed[i]
                tm = (target - p)/spd
                print(p, tm)
                if tm > prevTm: 
                    prevTm = tm
                    cnt += 1
            
            return cnt

