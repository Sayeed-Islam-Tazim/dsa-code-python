def rotate_matrix(matrix):
    n = len(matrix)
    result = [[0 for _ in range(n)] for _ in range(n)]    
    
    for i in range(n):
        for j in range(n):
            result[j][(n-i)-1] = matrix[i][j]
    return result
    
    
matrices = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10 ,11, 12],
    [13, 14, 15, 16]
]
print(rotate_matrix(matrices))