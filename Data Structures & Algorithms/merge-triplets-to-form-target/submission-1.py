class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        validTripletValue = [False] * 3

        for triplet in triplets:
            if triplet[0] > target[0]: continue
            if triplet[1] > target[1]: continue
            if triplet[2] > target[2]: continue

            if triplet[0] == target[0]: validTripletValue[0] = True
            if triplet[1] == target[1]: validTripletValue[1] = True
            if triplet[2] == target[2]: validTripletValue[2] = True

        return False not in validTripletValue