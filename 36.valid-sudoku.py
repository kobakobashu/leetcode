#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column = defaultdict(set)
        row = defaultdict(set)
        group = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in row[i]:
                        return False
                    row[i].add(board[i][j])
                    
                    if board[i][j] in column[j]:
                        return False
                    column[j].add(board[i][j])
                    
                    if board[i][j] in group[i // 3 + (j // 3) * 3]:
                        return False
                    group[i // 3 + (j // 3) * 3].add(board[i][j])

        return True
# @lc code=end

