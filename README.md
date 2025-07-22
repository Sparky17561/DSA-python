# DSA in Python

A comprehensive guide to Data Structures and Algorithms implementations in Python with time and space complexity analysis.

## Table of Contents

- [Time Complexity](#time-complexity)
- [Number Operations](#number-operations)
- [Array Operations](#array-operations)
- [Hashing](#hashing)
- [Recursion](#recursion)
- [String Operations](#string-operations)

## Time Complexity

### Rules for Time Complexity Analysis

1. **Always calculate Time complexity in worst case**
2. **Avoid Constant values and Lower values**

### Types of Time Complexity

- **Big-Oh (O)** - Worst case (Upper bound)
- **Theta (Θ)** - Average case
- **Omega (Ω)** - Best case (Lower bound)

## Number Operations

### Count Digits
**TC: O(log n) | SC: O(1)**

```python
from math import log10

def countDigits(num):
    return int(log10(num) + 1)
```

### Check Palindrome Number
**TC: O(log n) | SC: O(1)**

```python
def isPalindrome(n):
    num = n 
    result = 0
    while num > 0:
        ld = num % 10
        result = (result * 10) + ld
        num = num // 10 
    return n == result
```

### Armstrong Number
**TC: O(log n) | SC: O(1)**

```python
def isArmstrong(n):
    num = n 
    total = 0
    nod = len(str(n))
    while num > 0:
        ld = num % 10
        total = total + (ld ** nod)
        num = num // 10
    return total == n
```

**Example:** 153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = 153

### Find Factors/Divisors

#### Brute Force Approach
**TC: O(n) | SC: O(k)**

```python
def getFactors(num):
    result = []
    for i in range(1, num + 1):
        if num % i == 0:
            result.append(i)
    return result
```

#### Better Approach
**TC: O(n/2) | SC: O(k)**

```python
def getFactors(num):
    result = []
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            result.append(i)
    result.append(num)
    return result
```

#### Optimal Approach
**TC: O(√n) + O(n log n) | SC: O(k)**

```python
from math import sqrt

def getFactors(num):
    result = []
    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            result.append(i)
            if num // i != i:
                result.append(num // i)
    result.sort()  # O(n log n) for sorting
    return result
```

## Hashing

### Method 1: Basic Dictionary
**TC: O(n) | SC: O(n)**

```python
def createFrequencyMap(nums):
    freq_map = {}
    for i in range(len(nums)):
        if nums[i] in freq_map:
            freq_map[nums[i]] += 1
        else:
            freq_map[nums[i]] = 1
    return freq_map
```

### Method 2: Using .get()
**TC: O(n) | SC: O(n)**

```python
def createFrequencyMap(nums):
    hash_map = {}
    n = len(nums)
    for i in range(n):
        hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1
    return hash_map
```

### Constraint-Based Hashing
**TC: O(N + M) | SC: O(1)** (when constraint is small)

```python
# Constraint: 1 <= num <= 10
def constraintHashing(nums, queries):
    hash_list = [0] * 11
    
    # Prestore values
    for num in nums:
        hash_list[num] += 1
    
    # Answer queries
    results = []
    for num in queries:
        if 1 <= num <= 10:
            results.append(hash_list[num])
        else:
            results.append(0)
    return results
```

## Recursion

### Factorial
**TC: O(n) | SC: O(n)**

```python
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)
```

### Reverse Array
**TC: O(n/2) | SC: O(n/2)**

```python
def reverseArray(nums, left, right):
    if left >= right:
        return
    nums[left], nums[right] = nums[right], nums[left]
    reverseArray(nums, left + 1, right - 1)
```

### Check Palindrome String
**TC: O(n/2) | SC: O(n/2)**

```python
def isPalindrome(s, left, right):
    if left >= right:
        return True 
    if s[left] == s[right]:
        return isPalindrome(s, left + 1, right - 1)
    else:
        return False
```

### Fibonacci Number
**TC: O(2^n) | SC: O(n)**

```python
def fibonacci(num):
    if num == 0 or num == 1:
        return num 
    return fibonacci(num - 1) + fibonacci(num - 2)
```

## Array Operations

### Find Largest Element
**TC: O(n) | SC: O(1)**

```python
def findLargest(nums):
    largest = float("-inf")
    n = len(nums)
    for i in range(n):
        largest = max(largest, nums[i])
    return largest
```

### Find Second Largest Element

#### Brute Force Approach
**TC: O(2n) | SC: O(1)**

```python
def findSecondLargest(nums):
    largest = float("-inf")
    s_largest = float("-inf")
    n = len(nums)
    
    # Find largest
    for i in range(n):
        largest = max(largest, nums[i])
    
    # Find second largest
    for i in range(n):
        if nums[i] > s_largest and nums[i] != largest:
            s_largest = nums[i]
    
    return s_largest
```

#### Optimal Approach
**TC: O(n) | SC: O(1)**

```python
def findSecondLargest(nums):
    largest = float("-inf")
    s_largest = float("-inf")
    
    for i in range(len(nums)):
        if nums[i] > largest:
            s_largest = largest
            largest = nums[i]
        elif nums[i] > s_largest and nums[i] != largest:
            s_largest = nums[i]
    
    return s_largest
```

### Check if Array is Sorted
**TC: O(n) | SC: O(1)**

```python
def isSorted(nums):
    n = len(nums)
    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
            return False 
    return True
```

### Remove Duplicates from Sorted Array

#### Brute Force
**TC: O(n) | SC: O(k)**

```python
def removeDuplicates(nums):
    freq_map = {}
    n = len(nums)
    
    for i in range(n):
        freq_map[nums[i]] = 0
    
    j = 0
    for k in freq_map:
        nums[j] = k
        j += 1
    return j
```

#### Optimal (Two Pointer)
**TC: O(n) | SC: O(1)**

```python
def removeDuplicates(nums):
    n = len(nums)
    if n == 1:
        return 1
    
    i = 0
    j = 1
    while j < n:
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
        j += 1
    return i + 1
```

### Array Rotation

#### Right Rotate by 1 Place
**TC: O(n) | SC: O(1)**

```python
def rightRotateByOne(nums):
    n = len(nums)
    temp = nums[n - 1]
    for i in range(n - 2, -1, -1):
        nums[i + 1] = nums[i]
    nums[0] = temp
```

#### Right Rotate by K Places

##### Brute Force
**TC: O(n²) | SC: O(1)**

```python
def rightRotate(nums, k):
    n = len(nums)
    rotations = k % n
    
    for _ in range(rotations):
        e = nums.pop()
        nums.insert(0, e)
```

##### Better (Slicing)
**TC: O(n) | SC: O(n)**

```python
def rightRotate(nums, k):
    n = len(nums)
    k = k % n
    nums[:] = nums[n - k:] + nums[:n - k]
```

##### Optimal (Reverse Method)
**TC: O(n) | SC: O(1)**

```python
def reverse(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

def rightRotate(nums, k):
    n = len(nums)
    k = k % n
    
    reverse(nums, n - k, n - 1)  # Reverse last K numbers 
    reverse(nums, 0, n - k - 1)  # Reverse remaining elements 
    reverse(nums, 0, n - 1)      # Reverse whole array
```

### Move Zeros to End
**TC: O(n) | SC: O(1)**

```python
def moveZeros(nums):
    if len(nums) == 1:
        return
    
    # Find first zero
    i = 0
    while i < len(nums):
        if nums[i] == 0:
            break
        i += 1
    
    if i == len(nums):
        return
    
    j = i + 1
    while j < len(nums):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        j += 1
```

### Merge Two Sorted Arrays (Without Duplicates)
**TC: O(n + m) | SC: O(n + m)**

```python
def mergeSortedArrays(nums1, nums2):
    result = []
    n, m = len(nums1), len(nums2)
    i = j = 0
    
    while i < n and j < m:
        if nums1[i] <= nums2[j]:
            if len(result) == 0 or result[-1] != nums1[i]:
                result.append(nums1[i])
            i += 1
        else:
            if len(result) == 0 or result[-1] != nums2[j]:
                result.append(nums2[j])
            j += 1
    
    while i < n:
        if len(result) == 0 or result[-1] != nums1[i]:
            result.append(nums1[i])
        i += 1
    
    while j < m:
        if len(result) == 0 or result[-1] != nums2[j]:
            result.append(nums2[j])
        j += 1
    
    return result
```

## String Operations

### Valid Palindrome

#### Built-in Function Approach
**TC: O(n) | SC: O(n)**

```python
def isPalindrome(s):
    newStr = ""
    for c in s:
        if c.isalnum():
            newStr += c.lower()
    return newStr == newStr[::-1]
```

#### Two Pointer Approach
**TC: O(n) | SC: O(1)**

```python
def alphaNum(c):
    return (ord('A') <= ord(c) <= ord('Z') or 
            ord('a') <= ord(c) <= ord('z') or 
            ord('0') <= ord(c) <= ord('9'))

def isPalindrome(s):
    l, r = 0, len(s) - 1
    
    while l < r:
        while l < r and not alphaNum(s[l]):
            l += 1
        while r > l and not alphaNum(s[r]):
            r -= 1
        
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True
```

## Contributing

Feel free to contribute by adding more algorithms, optimizing existing solutions, or improving documentation.

## License

This project is open source and available under the MIT License.