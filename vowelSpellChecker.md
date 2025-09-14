# Spellchecker Problem

## Problem Description

Given a wordlist and a list of queries, implement a spellchecker that returns corrections for each query based on the following priority rules:

1. **Exact Match**: If the query appears exactly in the wordlist (case-sensitive), return it as-is
2. **Case-Insensitive Match**: If the query matches a word in the wordlist when both are converted to lowercase, return the first such word from the wordlist
3. **Vowel-Error Match**: If the query matches a word when both are converted to lowercase and all vowels (a, e, i, o, u) are replaced with wildcards, return the first such word from the wordlist
4. **No Match**: If none of the above rules apply, return an empty string

## Examples

### Example 1
```
Input: 
wordlist = ["KiTe", "kite", "hare", "Hare"]
queries = ["kite", "Kite", "KiTe", "Hare", "HARE", "Hear", "hear", "keti", "keet", "keto"]

Output: 
["kite", "KiTe", "KiTe", "Hare", "hare", "", "", "KiTe", "", "KiTe"]
```

**Explanation:**
- `"kite"`: Exact match found → `"kite"`
- `"Kite"`: Case-insensitive match with `"kite"` → `"KiTe"` (first occurrence)
- `"KiTe"`: Exact match found → `"KiTe"`
- `"Hare"`: Exact match found → `"Hare"`
- `"HARE"`: Case-insensitive match with `"hare"` → `"hare"` (first occurrence)
- `"Hear"`: No match → `""`
- `"hear"`: No match → `""`
- `"keti"`: Vowel-error match with `"kite"` (`k*t*` pattern) → `"KiTe"` (first occurrence)
- `"keet"`: No match (different pattern `k**t`) → `""`
- `"keto"`: Vowel-error match with `"kite"` (`k*t*` pattern) → `"KiTe"` (first occurrence)

## Algorithm Overview

### 🔑 Key Insight
The solution uses three different matching strategies with decreasing priority:
1. Exact string matching (highest priority)
2. Case-insensitive matching 
3. Vowel-pattern matching (lowest priority)

### ⚙️ Approach

**Phase 1: Preprocessing the Wordlist**
1. Create a set for exact lookups: `exact = {word1, word2, ...}`
2. Create case-insensitive mapping: `caseMap[lowercase] = first_original_word`
3. Create vowel-pattern mapping: `vowelMap[devoweled_pattern] = first_original_word`

**Phase 2: Processing Queries**
For each query, check in priority order:
1. If `query` exists in `exact` → return `query`
2. If `query.lower()` exists in `caseMap` → return `caseMap[query.lower()]`
3. If `deVowel(query.lower())` exists in `vowelMap` → return `vowelMap[deVowel(query.lower())]`
4. Otherwise → return `""`

### 🎯 Vowel Replacement Strategy
The `deVowel` function replaces all vowels (a, e, i, o, u) with `*` to create a pattern:
- `"kite"` → `"k*t*"`
- `"keti"` → `"k*t*"`
- `"keto"` → `"k*t*"`

This allows matching words that differ only in vowels.

## Complexity Analysis

### ⏱️ Time Complexity
- **Preprocessing**: O(N × L) where N = wordlist size, L = max word length
- **Query Processing**: O(M × L) where M = queries size
- **Total**: O((N + M) × L)

With constraints N, M ≤ 5000 and L ≤ 7, this is very efficient.

### 💾 Space Complexity
- O(N × L) for storing:
  - Exact words set
  - Case-insensitive mapping
  - Vowel-pattern mapping
- Effectively O(N) since L ≤ 7 is constant

## Implementation Details

### Data Structures Used
- `set`: For O(1) exact lookups
- `dict`: For O(1) case-insensitive and vowel-pattern lookups
- Priority is maintained by the order of checking conditions

### Edge Cases Handled
- Empty queries
- Words with no vowels
- Duplicate words in wordlist (only first occurrence matters)
- Case variations
- Multiple possible vowel corrections

## Solution Code

```python
class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        Spellchecker that handles exact, case-insensitive, and vowel-error matches
        
        :type wordlist: List[str] - Dictionary of valid words
        :type queries: List[str] - Words to spell-check
        :rtype: List[str] - Corrected words or empty strings if no match
        """
        
        def deVowel(s):
            """
            Helper function to replace all vowels with '*' wildcard
            
            Example: "kite" -> "k*t*", "hello" -> "h*ll*"
            This allows matching words that differ only in vowels
            
            :param s: Input string
            :return: String with vowels replaced by '*'
            """
            return ''.join('*' if c in 'aeiou' else c for c in s)

        # ==================== PREPROCESSING PHASE ====================
        
        # 1. EXACT MATCH: Store all words in a set for O(1) lookup
        # This handles case-sensitive exact matches
        exact = set(wordlist)
        
        # 2. CASE-INSENSITIVE MATCH: Map lowercase -> original word
        # Only store the FIRST occurrence of each lowercase pattern
        caseMap = {}
        
        # 3. VOWEL-ERROR MATCH: Map devoweled pattern -> original word  
        # Only store the FIRST occurrence of each vowel pattern
        vowelMap = {}

        # Process each word in the wordlist to build our lookup structures
        for w in wordlist:
            # Convert to lowercase for case-insensitive matching
            lower = w.lower()
            
            # Create vowel pattern for vowel-error matching
            devowel = deVowel(lower)
            
            # Store case-insensitive mapping (only first occurrence)
            # This ensures we return the first word that matches case-insensitively
            if lower not in caseMap:
                caseMap[lower] = w
            
            # Store vowel-pattern mapping (only first occurrence)
            # This ensures we return the first word that matches the vowel pattern
            if devowel not in vowelMap:
                vowelMap[devowel] = w
        
        # ==================== QUERY PROCESSING PHASE ====================
        
        result = []
        
        # Process each query according to priority rules
        for q in queries:
            
            # PRIORITY 1: EXACT MATCH (case-sensitive)
            # If query exists exactly in wordlist, return it as-is
            if q in exact:
                result.append(q)
            else:
                # Prepare lowercase and devoweled versions for further checking
                lower = q.lower()
                devowel = deVowel(lower)
                
                # PRIORITY 2: CASE-INSENSITIVE MATCH
                # Check if lowercase version exists in our case mapping
                if lower in caseMap:
                    result.append(caseMap[lower])
                
                # PRIORITY 3: VOWEL-ERROR MATCH  
                # Check if vowel pattern exists in our vowel mapping
                elif devowel in vowelMap:
                    result.append(vowelMap[devowel])
                
                # PRIORITY 4: NO MATCH
                # If no rules apply, return empty string
                else:
                    result.append("")
                    
        return result
```

## Code Walkthrough

### Step-by-Step Execution Example

Let's trace through an example:

```python
wordlist = ["KiTe", "kite", "hare", "Hare"]
queries = ["kite", "Kite", "keti"]
```

**PREPROCESSING PHASE:**

1. **Building `exact` set:**
   ```python
   exact = {"KiTe", "kite", "hare", "Hare"}
   ```

2. **Building `caseMap` (case-insensitive mapping):**
   ```python
   # Processing each word:
   # "KiTe" -> lower="kite" -> caseMap["kite"] = "KiTe" (first occurrence)
   # "kite" -> lower="kite" -> already exists, skip
   # "hare" -> lower="hare" -> caseMap["hare"] = "hare" 
   # "Hare" -> lower="hare" -> already exists, skip
   
   caseMap = {"kite": "KiTe", "hare": "hare"}
   ```

3. **Building `vowelMap` (vowel-pattern mapping):**
   ```python
   # Processing each word:
   # "KiTe" -> lower="kite" -> deVowel="k*t*" -> vowelMap["k*t*"] = "KiTe"
   # "kite" -> lower="kite" -> deVowel="k*t*" -> already exists, skip
   # "hare" -> lower="hare" -> deVowel="h*r*" -> vowelMap["h*r*"] = "hare"
   # "Hare" -> lower="hare" -> deVowel="h*r*" -> already exists, skip
   
   vowelMap = {"k*t*": "KiTe", "h*r*": "hare"}
   ```

**QUERY PROCESSING PHASE:**

1. **Query "kite":**
   ```python
   # Check: "kite" in exact? YES!
   # Result: "kite"
   ```

2. **Query "Kite":**
   ```python
   # Check: "Kite" in exact? NO
   # Check: "kite" (lowercase) in caseMap? YES!
   # Result: caseMap["kite"] = "KiTe"
   ```

3. **Query "keti":**
   ```python
   # Check: "keti" in exact? NO
   # Check: "keti" (lowercase) in caseMap? NO
   # Check: "k*t*" (devoweled) in vowelMap? YES!
   # Result: vowelMap["k*t*"] = "KiTe"
   ```

**Final Result:** `["kite", "KiTe", "KiTe"]`

## Key Implementation Insights

### 🔑 Why This Solution Works

1. **Smart Data Structure Choice:**
   - `set` for O(1) exact lookups
   - `dict` for O(1) pattern-based lookups
   - Preprocessing once, query many times efficiently

2. **First-Occurrence Priority:**
   ```python
   if lower not in caseMap:
       caseMap[lower] = w  # Only store first occurrence
   ```
   This ensures we always return the first matching word from the wordlist.

3. **Elegant Priority Chain:**
   ```python
   if q in exact:                    # Priority 1: Exact
       result.append(q)
   elif lower in caseMap:           # Priority 2: Case-insensitive  
       result.append(caseMap[lower])
   elif devowel in vowelMap:        # Priority 3: Vowel-error
       result.append(vowelMap[devowel])
   else:                            # Priority 4: No match
       result.append("")
   ```

4. **Vowel Normalization Strategy:**
   ```python
   def deVowel(s):
       return ''.join('*' if c in 'aeiou' else c for c in s)
   ```
   - Simple but powerful: converts "kite", "keto", "kati" all to "k*t*"
   - Allows flexible vowel-error matching

## Constraints
- 1 ≤ wordlist.length, queries.length ≤ 5000
- 1 ≤ wordlist[i].length, queries[i].length ≤ 7
- wordlist[i] and queries[i] consist only of English letters