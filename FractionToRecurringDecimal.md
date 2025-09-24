# Fraction to Recurring Decimal

## Problem Statement

Given two integers representing the `numerator` and `denominator` of a fraction, return the fraction in string format. If the fractional part is repeating, enclose the repeating part in parentheses.

### Examples
- `1/2 = "0.5"` (terminating decimal)
- `2/1 = "2"` (whole number)
- `4/333 = "0.(012)"` (repeating decimal)
- `1/6 = "0.1(6)"` (mixed: non-repeating + repeating)

### Constraints
- `-2³¹ <= numerator, denominator <= 2³¹ - 1`
- `denominator != 0`
- Answer length guaranteed < 10⁴

## The Core Insight

**We are simulating manual long division step by step.**

The key insight for detecting repeating decimals:
> **If we ever encounter the same remainder twice during division, we've found a repeating cycle.**

Why? Because the remainder determines what happens next in division. Same remainder = same future digits.

## Algorithm Breakdown

### Step 1: Handle Special Cases
```python
if numerator == 0:
    return "0"
```

### Step 2: Handle Sign
```python
if (numerator < 0) ^ (denominator < 0):
    res.append("-")
```
Use XOR to check if exactly one number is negative.

### Step 3: Integer Part
```python
res.append(str(numerator // denominator))
remainder = numerator % denominator
```

### Step 4: Fractional Part (The Heart of the Algorithm)
```python
remainder_map = {}  # Maps remainder → position in result

while remainder != 0:
    # Check if we've seen this remainder before
    if remainder in remainder_map:
        idx = remainder_map[remainder]
        res.insert(idx, "(")      # Start of repeating cycle
        res.append(")")           # End of repeating cycle
        break
    
    # Store current remainder and its position
    remainder_map[remainder] = len(res)
    
    # Perform long division step
    remainder *= 10
    res.append(str(remainder // denominator))
    remainder %= denominator
```

## Detailed Walkthrough: `1/6 = "0.1(6)"`

| Step | remainder | remainder_map | remainder×10 | digit | new remainder | result |
|------|-----------|---------------|--------------|-------|---------------|---------|
| Start | 1 | `{}` | | | | `["0", "."]` |
| 1 | 1 | Store `{1: 2}` | 10 | 1 | 4 | `["0", ".", "1"]` |
| 2 | 4 | Store `{1: 2, 4: 3}` | 40 | 6 | 4 | `["0", ".", "1", "6"]` |
| 3 | 4 | **Found repeat!** | | | | Insert "(" at idx=3 |

Final result: `["0", ".", "1", "(", "6", ")"]` → `"0.1(6)"`

## Another Example: `4/333 = "0.(012)"`

| Step | remainder | Action | remainder×10 | digit | new remainder | result |
|------|-----------|---------|--------------|-------|---------------|---------|
| Start | 4 | | | | | `["0", "."]` |
| 1 | 4 | Store at idx=2 | 40 | 0 | 40 | `["0", ".", "0"]` |
| 2 | 40 | Store at idx=3 | 400 | 1 | 67 | `["0", ".", "0", "1"]` |
| 3 | 67 | Store at idx=4 | 670 | 2 | 4 | `["0", ".", "0", "1", "2"]` |
| 4 | 4 | **Repeat found!** | | | | Insert "(" at idx=2 |

Final result: `["0", ".", "(", "0", "1", "2", ")"]` → `"0.(012)"`

## Complete Solution with Comments

```python
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        # Handle zero numerator
        if numerator == 0:
            return "0"

        res = []
        
        # Handle negative sign (exactly one negative number)
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")
        
        # Work with absolute values from now on
        numerator, denominator = abs(numerator), abs(denominator)

        # Add integer part
        res.append(str(numerator // denominator))
        remainder = numerator % denominator
        
        # If no remainder, it's a whole number
        if remainder == 0:
            return "".join(res)
        
        # Add decimal point
        res.append(".")

        # Track remainders and their positions for cycle detection
        remainder_map = {}

        # Perform long division until remainder is 0 or we find a cycle
        while remainder != 0:
            # If we've seen this remainder before, we found a repeating cycle
            if remainder in remainder_map:
                idx = remainder_map[remainder]  # Where the cycle started
                res.insert(idx, '(')            # Mark start of cycle
                res.append(')')                 # Mark end of cycle
                break
            
            # Remember this remainder and where we are in the result
            remainder_map[remainder] = len(res)

            # Standard long division step:
            remainder *= 10                              # Bring down a zero
            res.append(str(remainder // denominator))    # Next digit
            remainder %= denominator                     # New remainder
        
        return "".join(res)
```

## Key Insights

1. **Remainder as State**: Each remainder represents the "state" of our division process
2. **Cycle Detection**: When a remainder repeats, we know the decimal will cycle
3. **Position Tracking**: We need to know WHERE the cycle started to place parentheses correctly
4. **Long Division Simulation**: `remainder *= 10` simulates bringing down a zero

## Time & Space Complexity

- **Time**: O(denominator) in worst case (when period length = denominator-1)
- **Space**: O(denominator) for the remainder_map

## Edge Cases Handled

- Zero numerator: `0/5 = "0"`
- Negative numbers: `-1/2 = "-0.5"`
- Whole numbers: `4/2 = "2"`
- Terminating decimals: `1/4 = "0.25"`
- Pure repeating: `1/3 = "0.(3)"`
- Mixed repeating: `1/6 = "0.1(6)"`