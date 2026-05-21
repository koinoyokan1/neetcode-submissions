
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        top, bottom = 0, len(matrix) - 1

        while top < bottom:
            for i in range(bottom - top):
                topLeft = matrix[top][top + i]
                matrix[top][top + i] = matrix[bottom - i][top]
                matrix[bottom-i][top] = matrix[bottom][bottom-i]
                matrix[bottom][bottom-i] = matrix[top+i][bottom]
                matrix[top+i][bottom] = topLeft

            top += 1
            bottom -= 1
        