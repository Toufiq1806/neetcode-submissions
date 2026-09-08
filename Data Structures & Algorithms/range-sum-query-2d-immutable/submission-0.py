class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix=matrix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        addup=[0]
        start_row=row1
        start_col=col1
        end_row=row2
        end_col=col2
        for i in range(start_row,end_row+1):
            for j in range(start_col,end_col+1):
                addup.append(addup[-1]+self.matrix[i][j])
        return addup[-1]

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)