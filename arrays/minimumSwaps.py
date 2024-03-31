def minimumSwaps(arr):
    swaps = 0
    visited = [False]*len(arr)
    for start_ind, start_val in enumerate(arr):
        if visited[start_ind]:
            pass
        else:
            cycle = [arr[start_ind]]
            visited[start_ind] = True
            ind = arr[start_ind] - 1 
            while arr[ind] != arr[start_ind]:
                visited[ind] = True
                cycle.append(arr[ind])
                ind = arr[ind] -1
            swaps += len(cycle) - 1
    return swaps
                

def test_0():
    arr = [4,3,1,2]
    assert minimumSwaps(arr) == 3

def test_1():
    arr = [7,1,3,2,4,5,6]
    assert minimumSwaps(arr) == 5

if __name__ == '__main__':
    test_0()
    test_1()