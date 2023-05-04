# Input: s1 = "rat", s2 = "art"
# Output: true
# Input: s1 = "cat", s2 = "rat"
# Output: false
#
import collections


def comp(a, b):
    a = list(a)
    b = list(b)
    c = []
    result = True
    frequencyA = collections.Counter(a)
    frequencyB = collections.Counter(b)
    if len(a) == len(b):
        if dict(frequencyA) == dict(frequencyB):
            for x in a:
                if x in b:
                    c.append(x)
                else:
                    result = False
                    break
            if a == c:
                result = True
        else:
            result = False
    else:
        result = False
    return result


print(comp("rat", "rta"))
