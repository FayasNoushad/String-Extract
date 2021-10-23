def lines(string):
    return len(string.split("\n"))


def space(string):
    return len(string.split()) - 1


def words(string):
    return len(string.split())


def links(string):
    total = []
    https = string.split("https://")
    for i in https:
        set = i.split("http://")
        for subset in set:
            total.append(subset)
    return len(total) - 1
