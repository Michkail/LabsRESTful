import re

if char := input():
    # x = char.replace("a", "").replace("i", "").replace("e", "")
    x = re.sub("[aie]", "", char)
    print(x)


