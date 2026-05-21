class CountSquares:
    def __init__(self):
        self.xy = defaultdict(set)   
        self.ptCnt = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.xy[point[0]].add(point[1])        
        self.ptCnt[(point[0], point[1])] += 1


    def count(self, point: List[int]) -> int:
        x, y = point[0], point[1]
        cnt = 0

        for y2 in self.xy[x]:
            pt1 = (point[0], point[1])
            pt2 = (point[0], y2)

            distToOtherPt = abs(y2 - y)

            pt3 = (x-distToOtherPt, y2)
            pt4 = (x-distToOtherPt, y)

            if pt3[1] in self.xy[pt3[0]] and pt4[1] in self.xy[pt4[0]]:
                print(pt1, pt2, pt3, pt4)
                if len(set([pt1, pt2, pt3, pt4])) == len([pt1, pt2, pt3, pt4]):
                    cnt += self.ptCnt[pt2] * self.ptCnt[pt3] * self.ptCnt[pt4]

            pt3 = (x+distToOtherPt, y2)
            pt4 = (x+distToOtherPt, y)

            if pt3[1] in self.xy[pt3[0]] and pt4[1] in self.xy[pt4[0]]: 
                print(pt1, pt2, pt3, pt4)
                if len(set([pt1, pt2, pt3, pt4])) == len([pt1, pt2, pt3, pt4]):
                    cnt += self.ptCnt[pt2] * self.ptCnt[pt3] * self.ptCnt[pt4]

        return cnt
