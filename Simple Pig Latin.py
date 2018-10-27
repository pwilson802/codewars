# https://www.codewars.com/kata/simple-pig-latin/train/python

import string

def pig_it(text):
    text_list = text.split()
    punc = string.punctuation
    for num, x in enumerate(text_list):
        if x in punc:
            continue
        else:
            text_list[num]= x[1:] + x[0] + 'ay'
    return ' '.join(text_list)


if __name__ == '__main__':
    result = pig_it('Pig latin is cool')
    result2 = pig_it('Hello world !')
    print(result)
    print(result2)