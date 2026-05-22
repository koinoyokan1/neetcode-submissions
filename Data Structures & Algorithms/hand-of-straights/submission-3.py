'''
1:0, 2:0, 3:0, 4:0 5:0
1,2,3,4,5
1,2,3,4

'''
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        handCntr = Counter(hand)
        hand.sort()
        start = 0

        if len(hand)% groupSize != 0: return False

        def findNxtN(start):
            for i in range(start, start+groupSize):
                if handCntr[i] == 0: return False
                handCntr[i] -= 1
            return True

        for h in hand:
            if handCntr[h] == 0: continue
            if not findNxtN(h): return False
        return True
