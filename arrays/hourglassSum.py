def hourglassSum(arr):
    max_value = -9*7
    for row in range(len(arr)-2):
        for col in range(len(arr[0])-2):
            val_i = arr[row][col] + arr[row][col+1] + arr[row][col+2]
            val_i += arr[row+1][col+1]
            val_i += arr[row+2][col] + arr[row+2][col+1] + arr[row+2][col+2]
            if val_i > max_value:
                max_value = val_i
    return max_value

def test_0():
    arr = [[1, 1, 1, 0, 0, 0], 
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0]]
    assert hourglassSum(arr) == 19

def test_1():
    arr = [[-9, -9, -9, 1, 1, 1],
           [0, -9, 0, 4, 3, 2],
           [-9, -9, -9, 1, 2, 3],
           [0, 0, 8, 6, 6, 0],
           [0, 0, 0, -2, 0, 0],
           [0, 0, 1, 2, 4, 0]]
    assert hourglassSum(arr) == 28

if __name__ == '__main__':
    test_0()
    test_1()