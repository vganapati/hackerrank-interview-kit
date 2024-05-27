import functools

def maxSubsetSum(arr):
    @functools.cache
    def maxSubsetSum(arr_tuple):
        if len(arr_tuple) == 0:
            return 0
        elif len(arr_tuple) == 1:
            if arr_tuple[0]>0:
                return arr_tuple[0]
            else:
                return 0
        elif len(arr_tuple) == 2:
            if max(arr_tuple)>0:
                return max(arr_tuple)
            else:
                return 0
        else:
            maxVal = max(maxSubsetSum(arr_tuple[:-1]), maxSubsetSum(arr_tuple[:-2]) + arr_tuple[-1])
            if maxVal > 0:
                return maxVal
            else:
                return 0
    arr_tuple = tuple(arr)
    return maxSubsetSum(arr_tuple)


def test_0():
    arr = [3, 7, 4, 6, 5]
    assert maxSubsetSum(arr) == 13

if __name__ == '__main__':
    test_0()