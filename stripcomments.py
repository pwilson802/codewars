# Strip Comments
# https://www.codewars.com/kata/strip-comments/train/python

def solution(string,markers):
    x = string.split('\n')
    for num,line in enumerate(x):
        for marker in markers:
            if marker in line:
                m_dex = line.index(marker)
                x[num] = line[:m_dex].strip()
    return '\n'.join(x)
