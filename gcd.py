                                
def find_gcd(a, b):
    # Continue loop as long as both
    # a and b are greater than 0
    while a > 0 and b > 0:
        # If a is greater than b,
        # subtract b from a and update a
        if a > b:
            # Update a to the remainder
            # of a divided by b
            a = a % b
        # If b is greater than or equal
        # to a, subtract a from b and update b
        else:
            # Update b to the remainder
            # of b divided by a
            b = b % a
    # Check if a becomes 0,
    # if so, return b as the GCD
    if a == 0:
        return b
    # If a is not 0,
    # return a as the GCD
    return a


def main():
    n1 = 7
    n2 = 9

    # Find the GCD of n1 and n2
    gcd = find_gcd(n1, n2)

    print(f"GCD of {n1} and {n2} is: {gcd}")


if __name__ == "__main__":
    main()
    
                                
                            