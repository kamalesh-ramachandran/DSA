class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            row_seen=set()
            for value in row:
                if value == ".":
                    continue
                if value in row_seen:
                    return False
                row_seen.add(value)
        for col in range(len(board)):
            col_seen=set()
            for row in range(len(board)):
                value=board[row][col]
                if value == ".":
                    continue
                if value in col_seen:
                    return False
                col_seen.add(value)
        for row_box in range(0,len(board),3):
            for col_box in range(0,len(board),3):
                box_seen=set()
                for row in range(row_box,row_box+3):
                    for col in range(col_box,col_box+3):
                        value=board[row][col]
                        if value == ".":
                            continue
                        if value in box_seen:
                            return False
                        box_seen.add(value)
        return True

                

            

