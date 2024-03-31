def rotLeft(a, d):
    d = d % len(a)
    return a[d:] + a[0:d]

def test_0():
    a = [1, 2, 3, 4, 5]
    d = 4
    assert rotLeft(a, d) == [5, 1, 2, 3, 4]

if __name__ == '__main__':
    test_0()