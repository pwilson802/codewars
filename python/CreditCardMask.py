# https://www.codewars.com/kata/credit-card-mask/train/python
# return masked string
def maskify(cc):
    hashes = ""
    for hash in cc[:-4]:
        hashes += '#'
    return hashes + cc[-4:]

test = maskify('123456789')
print(test)