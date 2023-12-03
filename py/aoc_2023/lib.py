import re

re_ints = re.compile(r"\d+")


def ints_from_str(s):
    print(s)
    return [int(x) for x in re_ints.findall(s)]
