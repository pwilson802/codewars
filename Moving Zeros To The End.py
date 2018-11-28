# https://www.codewars.com/kata/moving-zeros-to-the-end

def move_zeros(array):
#    zeros = array.count(0)
    non_zero = [x for x in array if str(x) != '0' and str(x) != '0.0']
    zeros = len(array) - len(non_zero)
    return non_zero + (zeros * [0])


if __name__ == '__main__':
    x = move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9])
    y = move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9])

    print(x)
    print(y)
