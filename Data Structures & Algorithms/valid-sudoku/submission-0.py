class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9) :
            s1 = set()
            s2 = set()
            s3 = set()
            for j in range(9) :
                if (board[i][j] != ".") and (board[i][j] in s1) :
                    return False

                if (board[j][i] != ".") and (board[j][i] in s2) :
                    return False

                if (board[j//3 + 3*(i//3)][j%3 + 3*(i%3)] != ".") and (board[j//3 + 3*(i//3)][j%3 + 3*(i%3)] in s3) :
                    return False  

                s1.add(board[i][j])
                s2.add(board[j][i])
                s3.add(board[j//3 + 3*(i//3)][j%3 + 3*(i%3)])    


        return True