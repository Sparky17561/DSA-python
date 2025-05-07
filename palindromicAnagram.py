def can_form_palindrome(s):
    # normalize (optional): here we lowercase and remove spaces;
    # remove or adjust this if you want to consider spaces/punctuation too
    s = s.replace(" ", "").lower()

    # 1) Build frequency map
    count = {}
    for c in s:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1

    # 2) At most one character may have an odd count
    odd_counts = 0
    for freq in count.values():
        if freq % 2 != 0:
            odd_counts += 1
            if odd_counts > 1:
                return False

    return True


if __name__ == "__main__":
    s = input("Enter a string: ")
    result = can_form_palindrome(s)
    print(result)   # True if some permutation of s is a palindrome, else False
