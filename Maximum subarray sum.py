# https://www.codewars.com/kata/maximum-subarray-sum/train/python

def maxSequence(arr):
    res = 0
    f = 0
    for num, x in enumerate(arr):
        if arr[f:num+1]




if __name__ == '__main__':
    a = maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print(a)