## Extract matched pattern from corpus based on regex

````
python3 extract_corpus_from_regex.py corpus.txt regex.txt
````


## Regular Expressions (Regex) Basics

Regex is a sequence of characters that defines a search pattern. Use it for text matching, validation, or extraction.

## Basic Syntax

### 1. Anchors
- `^` Start of line
- `$` End of line

**Example**:  
`^Hello` matches "Hello" at the start of a string.  
`world$` matches "world" at the end.

---

### 2. Quantifiers
- `*` 0 or more
- `+` 1 or more
- `?` 0 or 1
- `{n}` Exactly `n` times

**Example**:  
`a+` matches "a", "aa", "aaa", etc.  
`\d{3}` matches exactly 3 digits (e.g., "123").

---

### 3. Character Classes
- `[abc]` Match a, b, or c
- `[a-z]` Match lowercase letters
- `\d` Digit (`[0-9]`)  
- `\w` Word character (`[a-zA-Z0-9_]`)  
- `.` Any character (except newline)

**Example**:  
`[A-Za-z]+` matches one or more letters (e.g., "Hello").

---

### 4. Groups and Alternation
- `(abc)` Capture group
- `|` OR operator

**Example**:  
`(cat|dog)` matches "cat" or "dog".

---

### 5. Escaping Special Characters
Use `\` to escape regex symbols like `.`, `*`, `?`, etc.

**Example**:  
`\d+\.\d+` matches decimals like "3.14".

### Tools & Resources

Online Testers: [Regex101](https://regex101.com/), [RegExr](https://regexr.com/)

Cheat Sheet: [Regex Quick Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Cheatsheet)

Natural language to regex: [EasyRegex](https://www.easyregex.com/regex/), [rows.com](https://rows.com/spreadsheet/regex-generator-1OsvySxsJUgr4lMPEPicChUuAp9pB9FtqlSXFkAQENxL/8c85da75-d3d2-49a7-80b3-94739a047d19#regex-generator-with-ai)
---

