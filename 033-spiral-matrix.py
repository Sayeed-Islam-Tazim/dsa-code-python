def spiral_matrix(matrix):
    result = []   
    top, left, right, bottom = 0, 0, len(matrix[0]) - 1, len(matrix) - 1

    while top <= bottom and left <= right:    
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        if top <= bottom:
            for i in range(right, left  - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
        
    print(result)
    return result
    
matrices1 = [
    [ 1,  2,  3,  4,  5,  6],
    [20, 21, 22, 23, 24,  7],
    [19, 32, 33, 34, 25,  8],
    [18, 31, 36, 35, 26,  9],
    [17, 30, 29, 28, 27, 10],
    [16, 15, 14, 13, 12, 11], 
] # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]

matrices2 = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12],
] # Output: [1,2,3,4,8,12,11,10,9,5,6,7] 

spiral_matrix(matrices2)