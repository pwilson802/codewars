# https://www.codewars.com/kata/directions-reduction/train/python

def dirReduc(arr):
    op = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    removals = []
    hit = False
    again = False
    for num, x in enumerate(arr[:-1]):
        if hit:
            hit = False
            continue
        if x == op[arr[num+1]]:
            removals.append(num)
            removals.append(num+1)
            hit = True
            again = True
    for index in sorted(removals, reverse=True):
        arr.pop(index)
    if again:
        arr = dirReduc(arr)
    return(arr)

if __name__ == '__main__':
    a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
    a_red = dirReduc(a)
    print(a_red)
    # A should be ['WEST'])

    u = ["NORTH", "WEST", "SOUTH", "EAST"]
    u_red = dirReduc(u)
    print(u_red)
    # U should be []