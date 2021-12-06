import re
import hashtags_extract


def lines(string):
    return len(string.split("\n"))


def words(string):
    return string.replace("\n", " ").split()


def spaces(string):
    return len(words(string)) - 1


def hashtags(string):
    return hashtags_extract.hashtags(string, hash=True)


def links(string):
    return re.findall(r'(https?://[^\s]+)', string)
