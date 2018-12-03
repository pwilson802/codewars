# https://www.codewars.com/kata/valid-parentheses/train/python

def valid_parentheses(s):
    brackets = "()"
    found_par = [x for x in s if x in brackets]
    for num, x in enumerate(found_par):
        if x == '('
            if ')' not in found_par[num:]:
                return False
    return True


if __name__ == "__main__":
    try1 = valid_parentheses(")test")
    print(try1)
    try2 = valid_parentheses("hi())(")
    print(try2)
    try3 = valid_parentheses("(ja)g(())(d)u")
    print(try3)