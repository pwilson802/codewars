# https://www.codewars.com/kata/scramblies/train/python
from collections import Counter

def scramble(s1, s2):
    base = Counter(s2)
    comparision = Counter(s1)
    for x in base:
        if x not in comparision:
            return False
        elif base[x] > comparision[x]:
            return False
    return True

if __name__ == '__main__':
    a = scramble('ccodewarsedewarccaaossoqqyt', 'codewars')
    print(a)