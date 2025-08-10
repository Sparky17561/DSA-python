Here’s a clean **README** you can use for your `FreqStack` implementation:

---

# 📦 FreqStack – Maximum Frequency Stack

## 📌 Overview

`FreqStack` is a special type of stack that supports two operations:

* **push(val)** – Pushes an integer onto the stack.
* **pop()** – Removes and returns the element with the **highest frequency**.
  If there’s a tie in frequency, it returns the **most recently pushed** among them.

This solves the ["Maximum Frequency Stack" problem](https://leetcode.com/problems/maximum-frequency-stack/) efficiently using **two hash maps** and a **max frequency tracker**.

---

## 🚀 How It Works

We maintain:

1. **`freq`** → Maps each element to its frequency.
2. **`m`** → Maps each frequency to a **stack** of elements with that frequency.
3. **`maxF`** → Tracks the current maximum frequency.

**Push Logic**

1. Increase `freq[val]`.
2. Update `maxF` if needed.
3. Append `val` to the list in `m[freq[val]]`.

**Pop Logic**

1. Pop the most recent element from `m[maxF]`.
2. Decrease its frequency in `freq`.
3. If `m[maxF]` becomes empty, decrement `maxF`.
4. Return the popped element.

---

## 🛠 Complexity

* **Push** → `O(1)`
* **Pop** → `O(1)`
* **Space** → `O(n)` for storing frequencies and stacks.

---

## 📄 Code

```python
from collections import defaultdict

class FreqStack(object):

    def __init__(self):
        self.m = defaultdict(list)  # frequency → stack of elements
        self.maxF = 0               # current maximum frequency
        self.freq = defaultdict(int) # element → frequency
        
    def push(self, val):
        self.freq[val] += 1
        self.maxF = max(self.maxF, self.freq[val])
        self.m[self.freq[val]].append(val)
        
    def pop(self):
        freq, m, maxF = self.freq, self.m, self.maxF
        x = m[maxF].pop()
        if not m[maxF]:
            self.maxF = maxF - 1
        freq[x] -= 1
        return x
```

---

## 📊 Example Usage

```python
fs = FreqStack()
fs.push(5)
fs.push(7)
fs.push(5)
fs.push(7)
fs.push(4)
fs.push(5)

print(fs.pop())  # 5 (freq=3)
print(fs.pop())  # 7 (freq=2, most recent)
print(fs.pop())  # 5
print(fs.pop())  # 4
```

**Output:**

```
5
7
5
4
```

---

## 🧠 Key Insight

The trick is to **group elements by frequency** instead of just pushing them in one stack.
This allows `pop()` to always work in `O(1)` time without scanning the whole stack.

---

Do you want me to also **add a diagram** showing how `m`, `freq`, and `maxF` change step-by-step during pushes and pops? That would make the README even more visual.
