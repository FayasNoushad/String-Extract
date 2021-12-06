# String Extract
Extract more items from string

## Installation

```
pip install String-Extract
```

## Usage

```py
import string_extract


string = """Hi [Fayas](https://github.com),

How are you?

#SupportOpensource"""
```

### Lines

```py
print(string_extract.lines(string))
# => 5
```

### Spaces

```py
print(string_extract.spaces(string))
# => 3
```

### Words

```py
print(string_extract.words(string))
# => ["Hi", ....]

print(len(string_extract.words(string)))
# => 6
```

### Hashtags

```py
print(string_extract.hashtags(string))
# => ["#SupportOpensource"]

print(len(string_extract.hashtags(string)))
# => 1
```

### Links

```py
print(string_extract.links(string))
# => ["https://github.com"]

print(len(string_extract.links(string)))
# => 1
```
