# 📁 Simplify Path - LeetCode 71

[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange.svg)](https://leetcode.com/problems/simplify-path/)
[![Topics](https://img.shields.io/badge/Topics-String%20%7C%20Stack-blue.svg)]()
[![Python](https://img.shields.io/badge/Language-Python-3776ab.svg)](https://www.python.org/)

## 🎯 Problem Statement

You are given an **absolute** path for a Unix-style file system, which always begins with a slash `'/'`. Your task is to transform this absolute path into its **simplified canonical path**.

### Unix File System Rules

| Symbol | Meaning | Action |
|--------|---------|--------|
| `'.'` | Current directory | Ignore (stay in same directory) |
| `'..'` | Parent directory | Go back one level |
| `'//'` or `'///'` | Multiple slashes | Treat as single `'/'` |
| `'...'`, `'....'` | Valid names | Treat as regular directory/file names |

### Canonical Path Requirements

✅ **Must start** with a single slash `'/'`  
✅ **Directories separated** by exactly one slash `'/'`  
✅ **Must not end** with slash `'/'` (unless root directory)  
✅ **No `'.'` or `'..'`** in the final path  

---

## 💡 Approach & Algorithm

### Core Insight
This is a perfect **Stack** problem! Think of the file system as a stack of directories:
- **Push** valid directory names onto the stack
- **Pop** when encountering `'..'` (go to parent)
- **Ignore** `'.'` and empty components (multiple slashes)

### Algorithm Steps

1. **Split the path** by `'/'` to get individual components
2. **Process each component**:
   - `''` (empty) or `'.'` → Skip (continue)
   - `'..'` → Pop from stack if not empty (go to parent)
   - Valid name → Push to stack (enter directory)
3. **Reconstruct path** by joining stack elements with `'/'`
4. **Add leading slash** to create absolute path

### Why Stack Works
- **LIFO nature** perfectly models directory navigation
- **Pop operation** handles `'..'` (parent directory) elegantly  
- **Push operation** builds the directory hierarchy
- **Final state** represents the canonical path

---

## 🔧 Complete Solution

```python
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        
        # Split path by '/' to get individual components
        components = path.split('/')

        for comp in components:
            # Skip empty components (from multiple slashes) and current directory
            if comp == '' or comp == '.':
                continue
                
            # Handle parent directory - go back one level
            if comp == '..':
                if stack:  # Only pop if stack is not empty
                    stack.pop()
            else:
                # Valid directory/file name - add to path
                stack.append(comp)
        
        # Reconstruct the canonical path
        return '/' + '/'.join(stack)
```

---

## 📊 Example Walkthrough

### Example 1: `path = "/home//foo/"`

**Step-by-step execution:**

1. **Split by '/':** `['', 'home', '', 'foo', '']`

2. **Process each component:**
   ```
   comp = '' → Skip (empty)
   stack = []
   
   comp = 'home' → Valid name, push
   stack = ['home']
   
   comp = '' → Skip (empty from //)
   stack = ['home']
   
   comp = 'foo' → Valid name, push  
   stack = ['home', 'foo']
   
   comp = '' → Skip (empty from trailing /)
   stack = ['home', 'foo']
   ```

3. **Reconstruct:** `'/' + '/'.join(['home', 'foo'])` = `"/home/foo"`

### Example 2: `path = "/a/./b/../../c/"`

**Visual stack operations:**

```
Input: "/a/./b/../../c/"
Split: ['', 'a', '.', 'b', '..', '..', 'c', '']

Step by step:
comp=''  →  []                    (skip empty)
comp='a' →  ['a']                 (push directory)
comp='.' →  ['a']                 (skip current dir)
comp='b' →  ['a', 'b']            (push directory) 
comp='..'→  ['a']                 (pop: go to parent)
comp='..'→  []                    (pop: go to parent)
comp='c' →  ['c']                 (push directory)
comp=''  →  ['c']                 (skip empty)

Result: "/" + "c" = "/c"
```

### Example 3: `path = "/../"`

**Edge case handling:**

```
Input: "/../"
Split: ['', '..', '']

comp=''  →  []     (skip empty)
comp='..'→  []     (try to pop, but stack empty - stay at root)
comp=''  →  []     (skip empty)

Result: "/" + "" = "/"  (root directory)
```

---

## 🎨 Visual Representation

```
Original Path: "/home//foo/../bar/./baz/"

    Split by '/'
         ↓
['', 'home', '', 'foo', '..', 'bar', '.', 'baz', '']

    Process with Stack
         ↓
    
''     →  []               (skip)
'home' →  ['home']         (push)
''     →  ['home']         (skip) 
'foo'  →  ['home','foo']   (push)
'..'   →  ['home']         (pop - go back)
'bar'  →  ['home','bar']   (push)
'.'    →  ['home','bar']   (skip)
'baz'  →  ['home','bar','baz'] (push)
''     →  ['home','bar','baz'] (skip)

    Join with '/'
         ↓
    "/home/bar/baz"
```

---

## ⚡ Complexity Analysis

- **Time Complexity:** O(n)
  - `split('/')` operation: O(n)
  - Processing each component: O(1) per component
  - `join()` operation: O(n)
  - Overall: O(n) where n is the length of input path

- **Space Complexity:** O(n)
  - Stack can hold at most O(n) directory names
  - Split array also takes O(n) space
  - In worst case (no `..` operations), stack size equals number of directories

---

## 🧠 Key Insights & Edge Cases

### Why This Solution is Elegant

1. **Natural mapping**: Stack operations mirror file system navigation
2. **Handles all edge cases**: Empty components, root directory, invalid parent references
3. **Clean separation**: Split → Process → Reconstruct pattern
4. **Robust**: Automatically handles multiple consecutive slashes

### Critical Edge Cases

| Input | Output | Reason |
|-------|--------|--------|
| `"/"` | `"/"` | Root directory |
| `"/../"` | `"/"` | Can't go above root |
| `"/home/"` | `"/home"` | Remove trailing slash |
| `"/a//b"` | `"/a/b"` | Collapse multiple slashes |
| `"/a/./b"` | `"/a/b"` | Skip current directory |
| `"/a/../"` | `"/"` | Navigate to parent |

### Alternative Approaches

1. **Manual string parsing**: More complex, error-prone
2. **Regex-based solution**: Harder to read and maintain  
3. **Recursive approach**: Overkill for this linear problem

---

## 🎯 Pattern Recognition

This problem showcases the **Stack for Path Processing** pattern:

```
🥞 Stack Pattern Applications:
├── File system navigation (this problem)
├── Expression evaluation  
├── Balanced parentheses
├── Undo operations
└── Browser history

📝 Key Stack Operations:
├── Push: Add valid elements
├── Pop: Remove/undo operations
├── Peek: Check current state
└── Empty check: Boundary conditions
```

---

## 🚀 Extensions & Variations

- **Relative paths**: Handle paths not starting with `'/'`
- **Windows paths**: Support backslash separators
- **Symbolic links**: Resolve link references
- **Path validation**: Check for invalid characters
- **Case sensitivity**: Handle different OS conventions

### Real-world Applications

- **Web servers**: URL canonicalization
- **File systems**: Path resolution
- **Build tools**: Dependency path resolution
- **IDEs**: Project navigation

This solution demonstrates how the right data structure (stack) can elegantly solve complex string manipulation problems that mirror real-world system behaviors! 📁✨