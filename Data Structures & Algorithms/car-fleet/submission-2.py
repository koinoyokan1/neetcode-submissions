# 3 4 5 6 7 8
# 4 4 4 4 4 4
# 2 2 
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
            position = [[position[i], i] for i in range(len(position))]
            position.sort(key=lambda k: k[0])

            stack = []

            for p in position:
                index = p[1] 
                spd = speed[index]

                timeToFinish = (target - p[0]) / spd
                while stack and stack[-1] <= timeToFinish:
                    stack.pop()
                stack.append(timeToFinish)

            return len(stack) 