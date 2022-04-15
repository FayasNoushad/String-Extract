import re


def lines(string):
    return len(string.split("\n")) + 1


def words(string):
    return string.split()


def spaces(string):
    return len(words(string)) - 1


def links(string):
    return re.findall(r'(https?://[^\s]+)', string)
