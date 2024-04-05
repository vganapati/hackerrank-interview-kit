import math

def countTriplets(arr, r):
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
                        for i in t_1_list[t_1_pointer:]:
                            for j in t_2_list[t_2_pointer:]:
                                if j > i:
                                    num_triplets += 1
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

if __name__ == '__main__':
    test_3()
    test_1()
    test_0()
    test_2()

