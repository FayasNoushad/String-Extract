import re


def lines(string):
    return len(string.split("\n"))


def spaces(string):
    return len(string.split()) - 1


def words(string):
    return len(string.split())


def links(string):
    total = 0
    https = string.split("https://")
    for i in https:
        set = i.split("http://")
        for subset in set:
            total += 1
    return total


def urls(string):
    return re.findall(r'(https?://[^\s]+)', string)
