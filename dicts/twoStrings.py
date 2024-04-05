def twoStrings(s1, s2):
    char_dict = set()
    for char in s1:
        char_dict.add(char)
    for char in s2:
        if char in char_dict:
            return("YES")
    return("NO")

def test_0():
    s1 = "and"
    s2 = "art"
    assert twoStrings(s1,s2) == "YES"

def test_1():
    s1 = "be"
    s2 = "cat"
    assert twoStrings(s1, s2) == "NO"

if __name__ == "__main__":
    test_0()
    test_1()