# https://www.codewars.com/kata/scramblies/train/python


def scramble(s1, s2):
    for x in s2:
        try:
            if s2.count(x) > s1.count(x):
                return False
            else:
                continue
        except:
            return False
    return True

if __name__ == '__main__':
    a = scramble('odewarsedewaraaossoqqyt', 'codewars')
    print(a)