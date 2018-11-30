# https://www.codewars.com/kata/rgb-to-hex-conversion/train/python

def rgb(r, g, b):
    res = []
    for x in (r,g,b):
        if x < 0:
            x = 0
        if x > 255:
            x = 255
        hex_value = hex(x)[2:]
        if len(hex_value) == 1:
            hex_value = '0' + hex_value
        res.append(hex_value.upper())
    return ''.join(res)


if __name__ == '__main__':
    a = rgb(-20,400,252)
    print(a)

