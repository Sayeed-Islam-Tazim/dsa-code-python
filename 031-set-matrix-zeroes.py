# def make_infinity(matrix, row, col):
#     for i in range(rows):
#         if matrix[i][col] != 0:
#             matrix[i][col] = float('inf')
#     for j in range(cols):
#         if matrix[row][j] != 0:
#             matrix[row][j] = float('inf')

def set_matrix_zeroes(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    row_track = [0 for _ in range(rows)]
    col_track = [0 for _ in range (cols)]
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                row_track[i] = -1
                col_track[j] = -1
    
    for i in range(rows):
        for j in range(cols):
            if row_track[i] == -1 or col_track[j] == -1:
                matrix[i][j] = 0
    return matrix
#     for i in range(rows):
#         for j in range(cols):
#             if matrix[i][j] == 0:
#                 make_infinity(matrix, i, j)
                
#     for i in range(rows):
#         for j in range(cols):
#             if matrix[i][j] == float('inf'):
#                 matrix[i][j] = 0
#     return matrix
    
matrices = [
    [7, 2, 4, 5],
    [1, 0, 3, 4],
    [5, 6, 0, 8],
    [7, 10, 11, 12]
]

print(set_matrix_zeroes(matrices))