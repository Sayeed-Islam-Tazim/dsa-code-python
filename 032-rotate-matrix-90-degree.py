def rotate_matrix(matrix):
    n = len(matrix)
    
    # Brute Firce Approach
    # result = [[0 for _ in range(n)] for _ in range(n)]    
    
    # for i in range(n):
    #     for j in range(n):
    #         result[j][(n-i)-1] = matrix[i][j]
    # return result
    
    # Transpose Matrux Approach
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse()
    return matrix
    
    
matrices = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10 ,11, 12],
    [13, 14, 15, 16]
]
print(rotate_matrix(matrices))