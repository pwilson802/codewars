# https://www.codewars.com/kata/iq-test/train/python

def iq_test(n):
    n2 = [int(i) % 2 for i in n.split()]
    oe = min(n2, key=n2.count)
    return n2.index(oe)+1


if __name__ == '__main__':
    a = iq_test("2 4 7 8 10")
    print(a)
    b = iq_test('1 1 1 3 2 7 9')
    print(b)