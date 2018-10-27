def arrange(strng):
    s = strng.split()
    my_sum = 'less_than'
    for num, x in enumerate(s):
        if num == len(s) - 1:
            break
        first_one = s[num]
        second_one = s[num+1]
        if my_sum == 'less_than':
            if len(first_one) > len(second_one):
                print(first_one)
                s[num] = second_one
                s[num+1] = first_one
            my_sum = 'more_than'
        elif my_sum == 'more_than':
            if len(first_one) < len(second_one):
                print(first_one)
                s[num] = second_one
                s[num+1] = first_one
            my_sum = 'less_than'
    for num, x in enumerate(s):
        if num == 0:
            s[num] = x.lower()
        elif num % 2 == 1:
            s[num] = x.upper()
        else:
            s[num] = x.lower()
            continue
    return ' '.join(s)






if __name__ == '__main__':
    res = arrange("who hit retaining The That a we taken")
    print(res)