def multiply_matrices(mat1,mat2):
    row1=len(mat1)
    cols1=len(mat1[0])
    row2=len(mat2)
    cols2=len(mat2[0])
    
    if row1 != cols2:
        return "Can't perform multiplication, no. of row of matrix 1 should be equal to no. of column of matrix 2"

    result = [[0 for i in range(row1)] for i in range(cols2)]
    
    for i in range(row1):
        for j in range(cols2):
            for k in range(row2):
                result[i][j] += mat1[i][k]*mat2[k][j]
    
    return result 
    
# Example matrices
matrix1 = [[1, 2, 3],
           [4, 5, 6]]

matrix2 = [[7, 8],
           [9, 10],
           [11, 12]]

product = multiply_matrices(matrix1,matrix2)

if isinstance(product,str):
    print(product)
    
else:
    for row in product:
        print(row)