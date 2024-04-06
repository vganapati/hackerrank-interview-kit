import math

def countTriplets(arr, r):
    num_triplets = 0
    right_dict = {}
    left_dict = {}
    for ind, num in enumerate(arr):
        if num in right_dict.keys():
            right_dict[num] += 1
        else:
            right_dict[num] = 1

    if r == 1:
        for num in right_dict.keys():
            num_triplets += math.comb(right_dict[num], 3)
    else:
        for ind,num in enumerate(arr):
            if num % r == 0:
                if num//r in left_dict.keys() and num*r in right_dict.keys():
                    num_triplets += left_dict[num//r]*right_dict[num*r]
            right_dict[num] -= 1
            if num in left_dict.keys():
                left_dict[num] += 1
            else:
                left_dict[num] = 1
    return num_triplets

def countTriplets_0(arr, r):
    num_dict = {}
    for ind, num in enumerate(arr):
        if num in num_dict.keys():
            num_dict[num] += [ind]
        else:
            num_dict[num] = [ind]

    num_triplets = 0
    for num in num_dict.keys():
        # check for triplet
        if num*r in num_dict.keys() and num*r*r in num_dict.keys():
            # how many triplets?
            if r == 1:
                num_triplets += math.comb(len(num_dict[num]), 3)
            else:
                t_0_list = num_dict[num]
                t_1_list = num_dict[num*r]
                t_2_list = num_dict[num*r*r]
                t_0_pointer = 0
                t_1_pointer = 0
                t_2_pointer = 0

                while t_0_pointer < len(t_0_list) and t_1_pointer < len(t_1_list) and t_2_pointer < len(t_2_list):
                    t_0 = t_0_list[t_0_pointer]
                    t_1 = t_1_list[t_1_pointer]
                    t_2 = t_2_list[t_2_pointer]
                    if t_1 < t_0:
                        t_1_pointer += 1
                    elif t_2 < t_1:
                        t_2_pointer += 1
                    else:
                        i = t_1_pointer
                        j = t_2_pointer
                        while i < len(t_1_list) and j < len(t_2_list):
                            if t_1_list[i] > t_2_list[j]:
                                j += 1
                            else:
                                num_triplets += len(t_2_list) - j
                                i += 1
                        t_0_pointer += 1
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

def test_3():
    arr = [1, 1000, 1000, 100, 100, 10, 100, 1000, 100, 1000, 10000, 100]
    r = 10
    assert countTriplets(arr, r) == 13

def test_3():
    arr = [1]*100
    r = 1
    assert countTriplets(arr, r) == 161700

if __name__ == '__main__':
    test_3()
    test_1()
    test_0()
    test_2()

