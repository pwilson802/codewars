# https://www.codewars.com/kata/sum-of-digits-slash-digital-root/train/python

def digital_root(n):
    sn = str(n)
    while len(sn) != 1:
        sn = str(sum([int(x) for x in sn]))
    return int(sn)


if __name__ == "__main__":
    a = digital_root(243)
    print(a)