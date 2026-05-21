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

        for _ in range(len(hand)//groupSize):
            for i in range(start, len(hand)):
                if handCntr[hand[i]] == 0: continue
                start = i
                break

            num = hand[start]
            for i in range(groupSize):
                if handCntr[num] > 0:
                    handCntr[num] -= 1
                else: return False
                num += 1

        return True

