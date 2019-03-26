# https://www.codewars.com/kata/calculator/train/python

class Calculator(object):
  def evaluate(self, string):
    numerals = string.split()
    while True:
        if len(numerals) == 1:
            return numberals[0]
        else:
            if ('*' in numerals) or ('//' in numerals):
                for num, x in enumerate(numerals):
                    if (x == '*') or (x == '//'):
                        if x == '*':
                            res = int(numerals[num-1]) * int(numerals[num+1])
                        else:
                            res = int(numerals[num-1]) / int(numerals[num+1])
                    if num == 1:
                        numerals = numerals[num+1:]
                        numerals.insert(0, res)
                    else:
                        numerals = numerals[:num-1] + numerals[num+1:]
                        numerals.insert(num-1, res)
            else:
                for num, x in enumerate(numerals):
                    if (x == '+') or (x == '-'):
                        if x == '+':
                            res = int(numerals[num-1]) + int(numerals[num+1])
                        else:
                            res = int(numerals[num-1]) - int(numerals[num+1])
                    if num == 1:
                        numerals = numerals[num+1:]
                        numerals.insert(0, res)
                    else:
                        numerals = numerals[:num-1] + numerals[num+1:]
                        numerals.insert(num-1, res)


assert Calculator().evaluate("2 / 2 + 3 * 4 - 6") == 7, 'Should equal 7'
