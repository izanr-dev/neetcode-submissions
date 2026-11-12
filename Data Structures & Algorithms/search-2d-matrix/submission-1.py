class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        left = 0
        right = len(matrix[0]) -1
        down = 0
        up = len(matrix) -1

        while down <= up:

            y = (up + down) // 2

            if target == matrix[y][left] or target == matrix[y][right]:
                return True

            elif target < matrix[y][left]:
                up = y - 1
        
            elif target > matrix[y][right]:
                down = y + 1

            else:
                while left <= right:

                    x = (left + right) // 2

                    if target == matrix[y][x]:
                        return True

                    if target > matrix[y][x]:
                        left = x + 1

                    elif target < matrix[y][x]:
                        right = x - 1

        return False
