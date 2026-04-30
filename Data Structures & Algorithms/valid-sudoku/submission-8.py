class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxMap = {}
        rowMap = {}
        colMap = {}

        for i in range(9):
            for j in range(9):
                currVal = board[i][j]

                if i not in rowMap:
                    rowMap[i] = []
                if j not in colMap:
                    colMap[j] = []

                if currVal in rowMap[i]:
                    return False
                elif (currVal != "."):
                    rowMap[i].append(currVal)
                
                if currVal in colMap[j]:
                    return False
                elif (currVal != "."):
                    colMap[j].append(currVal)

        for i in range(9):
                boxMap[i] = []
                for r in range(3):
                    for c in range(3):
                        row = (i//3) * 3 + r
                        col = (i % 3) * 3 + c
                        if board[row][col] in boxMap[i]:
                            return False
                        if board[row][col] == ".":
                            continue
                        boxMap[i].append(board[row][col])
        return True
                