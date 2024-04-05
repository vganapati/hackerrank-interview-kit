import math

# need to add requirement i < j < k

def countTriplets(arr, r):
    num_dict = {}
    for num in arr:
        if num in num_dict.keys():
            num_dict[num] += 1
        else:
            num_dict[num] = 1

    num_triplets = 0
    for num in list(num_dict.keys()):
        # check for triplet
        if num*r in num_dict.keys() and num*r*r in num_dict.keys():
            # how many triplets?
            if r == 1:
                num_triplets += math.comb(num_dict[num], 3)
            else:
                t_0 = num_dict[num]
                t_1 = num_dict[num*r]
                t_2 = num_dict[num*r*r]
                num_triplets += t_0*t_1*t_2
    return num_triplets

def test_0():
    arr = [1,2,2,4]
    r = 2
    assert countTriplets(arr, r) == 2

def test_1():
    arr = [1, 3, 9, 9, 27, 81]
    r = 3
    assert countTriplets(arr, r) == 6

def test_2():
    arr = [1, 5, 5, 25, 125]
    r = 5
    assert countTriplets(arr, r) == 4

if __name__ == '__main__':
    test_1()
    test_0()
    test_2()

