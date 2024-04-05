import math
def sherlockAndAnagrams(s):
    num_anagrams = 0
    substrings = {}
    for substring_size in range(1, len(s)):
        for i in range(len(s[0:len(s)-substring_size+1])):
            key = tuple(sorted(s[i:i+substring_size]))
            if key in substrings.keys():
                substrings[key] += 1
            else:
                substrings[key] = 1
    for key in substrings.keys():
        num_anagrams += math.comb(substrings[key],2)
    return num_anagrams


def test_0():
    s = "abba"
    assert sherlockAndAnagrams(s) == 4

def test_1():
    s = "abcd"
    assert sherlockAndAnagrams(s) == 0

def test_2():
    s = "kkkk"
    assert sherlockAndAnagrams(s) == 10

if __name__ == "__main__":
    test_2()
    test_0()
    test_1()
    