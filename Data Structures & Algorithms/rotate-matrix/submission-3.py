
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        top, bottom = 0, len(matrix) - 1
        while top < bottom:
            for i in range(bottom - top):

                # save the topleft
                topLeft = matrix[top][top + i]

                # move bottom left into top left
                matrix[top][top + i] = matrix[bottom - i][top]

                # move bottom right into bottom left
                matrix[bottom - i][top] = matrix[bottom][bottom - i]

                # move top right into bottom right
                matrix[bottom][bottom - i] = matrix[top + i][bottom]

                # move top left into top right
                matrix[top + i][bottom] = topLeft
            bottom -= 1
            top += 1