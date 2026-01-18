def lower_triangle(nums):
    rows = len(nums)
    cols = len(nums[0]) if rows > 0 else 0
    for i in range(rows):
        
        for j in range(cols):
        # Upper Triangle
            # if i <= j:
            #     print(nums[i][j], end=" ")
            # else:   
            #     print("*", end=" ")
        
        # Lower Triangle
            # if i >= j:
            #     print(nums[i][j], end=" ")
            # else:   
            #     print("*", end=" ")
        
        # Diagonal of a Triangle
            # if i == j:
            #     print(nums[i][j], end=" ")
            #     # print("*", end=" ")
            # else:   
            #     print("*", end=" ")
            #     # print(nums[i][j], end=" ")
                
        # Other Diagonal of a Triangle
            if i + j == rows - 1:
                print(nums[i][j], end=" ")
            else:   
                print("*", end=" ")      
        print()
    
    # Transpose of a Matrix
    result = [ [0] * rows for _ in range(cols) ]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = nums[i][j]
        print('\n', result[i])
    
arr1 =  [   
            [1, 2, 3],
            [4, 5, 6], 
            [7, 8, 9]
        ]   
    
lower_triangle(arr1)