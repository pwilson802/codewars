# https://www.codewars.com/kata/maximum-subarray-sum/train/python

def maxSequence(arr):
    current_largest = 0
    for x, num in enumerate(arr):
        running_num = num
        if running_num > current_largest:
            current_largest = running_num
        for i in arr[x+1:]:
            running_num += i
            if running_num > current_largest:
                current_largest = running_num
    return current_largest

p = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
res = maxSequence(p)
print(res)






	