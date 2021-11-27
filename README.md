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


print(string_extract.lines(string))
# => 5

print(string_extract.spaces(string))
# => 3

print(string_extract.words(string))
# => 5

print(string_extract.hashtags(string))
# => ["#SupportOpensource"]

print(string_extract.total_hashtags(string))
# => 1

print(string_extract.links(string))
# => 1

print(string_extract.urls(string))
# => ["https://github.com"]
```
