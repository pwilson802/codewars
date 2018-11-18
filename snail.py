# https://www.codewars.com/kata/snail

def snail(array):
    res = []
    turn = 0
    while True:
        sides = len(array[0])
        # Find the Top
        top = array[0]
        # Find the right except the top box
        right = []
        for x in range(sides)[1:]:
            right.append(array[x][-1])
        # Get the bottom except for the right box
        bottom = array[-1][:-1]
        bottom.reverse()
        # Find the bottom
        left = []
        for x in range(1,sides-1):
            left.append(array[x][0])
        left.reverse()
        res = res + top + right + bottom + left
        # if the sides are greater than 3, remove the sides and start again
        if sides > 3:
            array = [x[1:-1] for x in array[1:-1]]
            continue
        elif sides == 2:
            return res
        elif sides == 3:
        # Get the middle
            middle = array[1][1]
            res.append(middle)
            return res


array = [[1,2,3],
         [4,5,6],
         [7,8,9]]

array2 = [[1,2,3,4],
         [5,6,7,8],
         [9,10,11,12],
         [13,14,15,16]]

bigger = [[x for x in range(300)] for x in range(300)]

result = snail(array)
result2 = snail(array2)
result3 = snail(bigger)

print(result)
print(result2)
print(result3)
