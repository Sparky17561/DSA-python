def mcp(inputs,weights,threshold):
    weighted_sum = sum(i*w for i,w in zip(inputs,weights))
    return 1 if weighted_sum >= threshold else 0

def AND_gate(x1,x2):
    return mcp([x1,x2],[1,1],threshold=2)

def OR_gate(x1,x2):
    return mcp([x1,x2],[1,1],threshold=1)

def NOT_gate(x1):
    return mcp([x1],[-1],threshold=0)

def ANDNOT_gate(x1, x2):
    return x1 and (1 - x2)  # x1 AND (NOT x2)

def NAND_gate(x1, x2): 
    return mcp([x1, x2], [-1, -1], threshold=-1) 

def XOR_gate(x1, x2):
    return OR_gate(ANDNOT_gate(x1, x2), ANDNOT_gate(x2, x1))

def XNOR_gate(x1, x2):
    return NOT_gate(XOR_gate(x1, x2))

def main():
    print("AND gate")
    for x1 in (0, 1):
        for x2 in (0, 1):
            print(f"{x1} AND {x2} = {AND_gate(x1, x2)}")

    print("\nOR gate")
    for x1 in (0, 1):
        for x2 in (0, 1):
            print(f"{x1} OR {x2} = {OR_gate(x1, x2)}")

    print("\nNOT gate")
    for x in (0, 1):
        print(f"NOT {x} = {NOT_gate(x)}")

    print("\nAND NOT gate (x1 AND NOT x2)")
    for x1 in (0, 1):
        for x2 in (0, 1):
            print(f"{x1} AND NOT {x2} = {ANDNOT_gate(x1, x2)}")

    print("\nXOR gate")
    for x1 in (0, 1):
        for x2 in (0, 1):
            print(f"{x1} XOR {x2} = {XOR_gate(x1, x2)}")



if __name__ == "__main__":
    main()
