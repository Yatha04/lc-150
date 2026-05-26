class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ans = True

        for i in range(len(board)):
            col = set()
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                if board[i][j] in col:
                    print(f"row {i} failed on {board[i][j]}")
                    ans = False
                else:
                    col.add(board[i][j])
        
        for i in range(len(board[0])):
            row = set()
            for j in range(len(board)):
                if board[j][i] == '.':
                    continue
                if board[j][i] in row:
                    print(f"col {i} failed on {board[i][j]}")
                    ans = False
                else:
                    row.add(board[j][i])
        
        for box in range(9):
            seen = set()
            for r in range((box // 3) * 3, (box // 3) * 3 + 3):
                for c in range((box % 3) * 3, (box % 3) * 3 + 3):
                    val = board[r][c]
                    if val == '.':
                        continue
                    if board[r][c] in seen:
                        print(f"box {box} failed on {val}")
                        ans = False
                    else:
                        seen.add(board[r][c])
        
        return ans