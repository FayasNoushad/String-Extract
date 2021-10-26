```
Made with Python3
(C) @FayasNoushad
Copyright permission under MIT License
License -> https://github.com/FayasNoushad/String-Extract/blob/main/LICENSE
```

---

## Installation

```
pip install String-Extract
```

---

## Usage

```py
from string_extract import lines, spaces, words, links, urls


string = """Hi [Fayas](https://fayas.me),

How are you"""
```

```py
print(lines(string))
# => 3
```

```py
print(spaces(string))
# => 3
```

```py
print(words(string))
# => 5
```

```py
print(links(string))
# => 1
```

```py
print(urls(string))
# ["https://fayas.me"]
```

---

## Credits

- [Fayas Noushad](https://github.com/FayasNoushad)

---
