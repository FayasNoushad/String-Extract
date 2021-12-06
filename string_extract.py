import re
import hashtags_extract


def lines(string):
    return len(string.split("\n"))


def spaces(string):
    return len(string.split()) - 1


def words(string):
    return string.replace("\n", " ").split()


def hashtags(string):
    return hashtags_extract.hashtags(string, hash=True)


def links(string):
    return re.findall(r'(https?://[^\s]+)', string)
