from collections import Counter

def letter_frequency(sentence):
    return Counter(sentence)

if __name__ == "__main__":
    response = [
        'vanilla',
        'chocolate',
        'vanilla',
        'vanilla',
        'vanilla',
        'caramel',
        'strawberry',
        'vanilla',
        'caramel'
    ]

    print(f"The children vote for {Counter(response).most_common(1)[0][0]} ice cream")
    print(Counter(response))
    print(Counter(response).most_common(1))
    print(Counter(response).most_common(1)[0])
    print(Counter(response).most_common(1)[0][0])
    