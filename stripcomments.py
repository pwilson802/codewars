# Strip Comments
# https://www.codewars.com/kata/strip-comments/train/python

def solution(string,markers):
    x = string.split('\n')
    l = []
    for num,line in enumerate(x):
        for marker in markers:
            if marker in line:
                m_dex = line.index(marker)
                print('{} -------{}'.format(m_dex, line))
                if line.index(marker) > 0:
                    l.append(line[:m_dex].strip())
                else:
                    continue
                # x[num] = line[:m_dex].strip()
    return '\n'.join(l)

y = "cherries pears , apples bananas\navocados cherries cherries pears ' strawberries\ncherries bananas oranges lemons =\n' strawberries avocados pears ! bananas"
x = ['#', "'", '-', '.', '?', ',', '!', '^', '@']
c = solution(y,x)
print(c)
