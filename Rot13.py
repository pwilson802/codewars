from codecs import encode as _dont_use_this_
import string
upper = string.ascii_uppercase * 2
lower = string.ascii_lowercase * 2

def rot13(message):
    res = ''
    for l in message:
        if l.lower() in lower:
            if l.islower():
                res += lower[lower.index(l) + 13]
            else:
                res += upper[upper.index(l) + 13]
        else:
            res += l
    return res

if __name__ == '__main__':
    print('should be grfg')
    a = rot13("Avoid success at all costs!")
    print(a)
    b = rot13("Test")
    print(b)