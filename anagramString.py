def is_anagram(st1, st2):
    if len(st1) != len(st2):
        return False

    count = {}

    for char in st1:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    for char in st2:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1

    return True

st1 = input().lower()
st2 = input().lower()

print(is_anagram(st1, st2))
