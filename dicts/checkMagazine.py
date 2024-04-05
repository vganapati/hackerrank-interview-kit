def checkMagazine(magazine, note):
    magazine = magazine.split(" ")
    available_words = {}
    for word in magazine:
        if word in available_words.keys():
            available_words[word] += 1
        else:
            available_words[word] = 1

    for word in note:
        if word in available_words.keys() and available_words[word] >= 1:
            available_words[word] -= 1
        else:
            return False
    return True

def test_0():
    magazine = "attack at dawn"
    note = "Attack at dawn"
    assert checkMagazine(magazine, note) == False

if __name__ == "__main__":
    test_0()