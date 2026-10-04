class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[[False]*9 for _ in range(9)]
        col=[[False]*9 for _ in range(9)]
        box=[[False]*9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if(board[i][j]!='.'):
                    num=ord(board[i][j])-ord('1')
                    boxIndex=(i//3)*3+(j//3)
                    if row[i][num] or col[j][num] or box[boxIndex][num]:
                        return False
                    row[i][num] = col[j][num] = box[boxIndex][num]=True
        return True
        