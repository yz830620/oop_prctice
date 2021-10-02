from collections import defaultdict


def letter_frequency(sentence):
    frequencies = {}
    for letter in sentence:
        frequency = frequencies.setdefault(letter, 0)
        frequencies[letter] = frequency + 1
    return frequencies

def letter_frequency2(sentence):
    # 構建元int 沒有傳入任何數字，就會回傳0
    frequencies = defaultdict(int)
    for letter in sentence:
        frequencies[letter] += 1
    return frequencies


if __name__ == "__main__":
    lf1 = letter_frequency("I am not so sure")
    lf2 = letter_frequency2("I am not so sure")
    assert lf1 == lf2
    print(lf1, lf2)