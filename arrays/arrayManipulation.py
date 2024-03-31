def arrayManipulation(n, queries):
    # prefix sum
    arr = [0]*n
    for query in queries:
        arr[query[0]-1] = arr[query[0]-1] + query[2]
        try:
            arr[query[1]] = arr[query[1]] - query[2]
        except IndexError:
            pass
    max_val = 0
    running_sum = 0
    for val in arr:
        running_sum += val
        if running_sum > max_val:
            max_val = running_sum
    return max_val

def arrayManipulation_0(n, queries):
    # brute force
    arr = [0]*n
    for query in queries:
        for ind in range(query[0]-1, query[1]):
            arr[ind] += query[2]
    return sorted(arr)[-1]



def test_0():
    n = 10
    queries = [[1,5,3],[4,8,7],[6,9,1]]
    assert arrayManipulation(n, queries) == 10

if __name__ == '__main__':
    test_0()