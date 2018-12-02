# https://www.codewars.com/kata/sum-of-digits-slash-digital-root/train/python

def digital_root(n):
    sn = str(n)
    if len(sn) == 1:
        return n
    else:
        new_num = sum([int(x) for x in sn ])
        digital_root(new_num)

if __name__ == "__main__":
    