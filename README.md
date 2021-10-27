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
import string_extract


string = """Hi [Fayas](https://fayas.me),

How are you"""
```

```py
print(string_extract.lines(string))
# => 3
```

```py
print(string_extract.spaces(string))
# => 3
```

```py
print(string_extract.words(string))
# => 5
```

```py
print(string_extract.links(string))
# => 1
```

```py
print(string_extract.urls(string))
# ["https://fayas.me"]
```

---

## Credits

- [Fayas Noushad](https://github.com/FayasNoushad)

---
