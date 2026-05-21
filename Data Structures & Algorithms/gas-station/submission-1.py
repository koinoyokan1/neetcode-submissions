'''
-1 0 -1 3
      2 3
'''
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
      if sum(gas) < sum(cost): return -1

      gas = [gas[i] - cost[i] for i in range(len(gas))]

      currGas = 0
      start = 0
      for i in range(len(gas)):
            g = gas[i]

            currGas += g
            if currGas < 0:
                  currGas = 0
                  start = i+1
            
      return start