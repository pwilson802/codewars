# https://www.codewars.com/kata/who-likes-it/train/python

def likes(names):
    if len(names) == 0:
        return 'no one likes this'
    elif len(names) == 1:
        return '{0[0]} likes this'.format(names)
    elif len(names) == 2:
        return '{0[0]} and {0[1]} like this'.format(names)
    elif len(names) == 3:
        return '{0[0]}, {0[1]} and {0[2]} like this'.format(names)
    else:
        others = len(names) - 2
        return '{0[0]}, {0[1]} and {1} others like this'.format(names, others)

if __name__ == '__main__':
    a = likes([])  # 'no one likes this')
    b = likes(['Peter'])  # 'Peter likes this')
    c = likes(['Jacob', 'Alex'])  # 'Jacob and Alex like this')
    d = likes(['Max', 'John', 'Mark'])  # 'Max, John and Mark like this')
    e = likes(['Alex', 'Jacob', 'Mark', 'Max'])  # 'Alex, Jacob and 2 others like this')
    for x in [a, b, c, d, e]:
        print(x)
