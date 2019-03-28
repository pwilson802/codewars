# https://www.codewars.com/kata/calculator/train/python

class Calculator(object):
  def evaluate(self, string):
    numerals = string.split()
    while True:
        if len(numerals) == 1:
            return numerals[0]
        else:
            if ('*' in numerals) or ('/' in numerals):
                for num, x in enumerate(numerals):
                    if (x == '*') or (x == '/'):
                        print(numerals)
                        if x == '*':
                            res = float(numerals[num-1]) * float(numerals[num+1])
                        else:
                            res = float(numerals[num-1]) / float(numerals[num+1])
                        if num == 1:
                            numerals = numerals[num+2:]
                            numerals.insert(0, res)
                            break
                        else:
                            numerals = numerals[:num-1] + numerals[num+2:]
                            numerals.insert(num-1, res)
                            break
            else:
                for num, x in enumerate(numerals):
                    if (x == '+') or (x == '-'):
                        print(numerals)
                        if x == '+':
                            res = float(numerals[num-1]) + float(numerals[num+1])
                        else:
                            res = float(numerals[num-1]) - float(numerals[num+1])
                        if num == 1:
                            numerals = numerals[num+2:]
                            numerals.insert(0, res)
                            break
                        else:
                            numerals = numerals[:num-1] + numerals[num+2:]
                            numerals.insert(num-1, res)
                            break


if __name__ == '__main__':
    assert Calculator().evaluate("2 / 2 + 3 * 4 - 6") == 7, 'Should equal 7'
    n = Calculator().evaluate("2 / 2 + 3 * 4 - 6")
    print(n)
