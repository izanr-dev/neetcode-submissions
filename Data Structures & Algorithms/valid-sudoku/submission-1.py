class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(len(board)):
            horizontal = []
            for number in board[i]:
                if (number != '.') and (number in horizontal):
                    return False
                else:
                    horizontal.append(number)

        for i in range(len(board)):
            vertical = []
            for j in range(len(board)):
                if (board[j][i] != '.' and board[j][i] in vertical):
                    return False
                else:
                    vertical.append(board[j][i])

        squares = [[], [], [], [], [], [], [], [], []]
        for i in range(len(board)):
            for j in range(len(board)):

                if (i < 3) and (j < 3):
                    if board[i][j] in squares[0] and board[i][j] != '.':
                        print(1)
                        return False
                    squares[0].append(board[i][j])

                elif (2 < i < 6) and (j < 3):
                    if board[i][j] in squares[1] and board[i][j] != '.':
                        print(2)
                        return False 
                    squares[1].append(board[i][j])

                elif (5 < i) and (j < 3):
                    if board[i][j] in squares[2] and board[i][j] != '.':
                        print(3)
                        return False
                    squares[2].append(board[i][j])

                elif (i < 3) and (2 < j < 6):
                    if board[i][j] in squares[3] and board[i][j] != '.':
                        print(4)
                        return False
                    squares[3].append(board[i][j])
                    print(board[i][j])

                elif (2 < i < 6) and (2 < j < 6):
                    if board[i][j] in squares[4] and board[i][j] != '.':
                        return False
                    squares[4].append(board[i][j])

                elif (5 < i) and (2 < j < 6):
                    if board[i][j] in squares[5] and board[i][j] != '.':
                        return False
                    squares[5].append(board[i][j])

                elif (i < 3) and (5 < j):
                    if board[i][j] in squares[6] and board[i][j] != '.':
                        return False
                    squares[6].append(board[i][j])

                elif (2 < i < 6) and (5 < j):
                    if board[i][j] in squares[7] and board[i][j] != '.':
                        return False
                    squares[7].append(board[i][j])

                elif (5 < i) and (5 < j):
                    if board[i][j] in squares[8] and board[i][j] != '.':
                        return False
                    squares[8].append(board[i][j])

        return True      
