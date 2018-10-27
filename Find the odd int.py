# https://www.codewars.com/kata/find-the-odd-int/train/python


def find_it(seq):
    return [x for x in seq if seq.count(x) % 2 == 1][0]


if __name__ == '__main__':
    tester = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
    result = find_it(tester)
    print(result)
