import re


def lines(string):
    return len(string.split("\n"))


def words(string):
    return string.replace("\n", " ").split()


def spaces(string):
    return len(words(string)) - 1


def links(string):
    return re.findall(r'(https?://[^\s]+)', string)
