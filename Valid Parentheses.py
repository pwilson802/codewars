# https://www.codewars.com/kata/valid-parentheses/train/python
def check_brackets(entry, direction):
    if direction == 'forwards':
        first = '('
        second = ')'
    elif direction == 'backwards':
        first = ')'
        second = '('
    count = 0
    for num, i in enumerate(entry):
        if i == first:
            closing = entry[num:]
            if closing.count(second) == 0:
                return False
            if closing.count(second) < count:
                return False
            else:
                count += 1
                continue
    return True

def valid_parentheses(string):
    brackets = "()"
    found_par = [x for x in string if x in brackets]
    # Check Forwards
    forward = check_brackets(found_par, 'forwards')
    found_par.reverse()
    backward = check_brackets(found_par, 'backwards')
    if forward and backward:
        return True
    else:
        return False





if __name__ == "__main__":
    try1 = valid_parentheses(")test")
    print(try1)
    try2 = valid_parentheses("hi())(")
    print(try2)