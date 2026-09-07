def transpose_matrix(mat):
    rows,cols=len(mat), len(mat[0])
    
    result= [[0 for i in range(rows)] for i in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            result[i][j]=mat[j][i]
    
    return result

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

transpose= transpose_matrix(matrix)

print("Original Matrix :")
for row in matrix:
    print(row)

print("Transposed Matrix :")
for row in transpose:
    print(row)