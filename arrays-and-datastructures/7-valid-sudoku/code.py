from collections import defaultdict

def validSudoku(mat):
    rows = defaultdict(set)
    cols = defaultdict(set)
    square = defaultdict(set)

    for r in range(9):
        for c in range(9):
            if mat[r][c] == ".":
                continue
            if(mat[r][c] in rows[r] or 
            mat[r][c] in cols[c] or
            mat[r][c] in square[(r // 3, c // 3)]):
                return False
            rows[r].add(mat[r][c])
            cols[c].add(mat[r][c])
            square[(r // 3, c // 3)].add(mat[r][c])
        print(rows)

    
    return True



    return res

def main():
    input = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

    print(f"Output = {validSudoku(input)}")
    return 0

if __name__ == "__main__":
    main()