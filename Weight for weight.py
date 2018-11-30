# https://www.codewars.com/kata/weight-for-weight/train/python

def order_weight(strng):
    weight_list = sorted(strng.split())
    return ' '.join(sorted(weight_list, key=lambda k: sum([int(x) for x in k])))



if __name__ == '__main__':
    a = order_weight("108 103 123 4444 99 2000 11")
    print(a)

