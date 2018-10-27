# https://www.codewars.com/kata/human-readable-time/train/python


def make_readable(seconds):
    hour = 60 * 60
    minute = 60
    second = 1
    res = []
    for metric in [hour, minute, second]:
        count = seconds // metric
        if len(str(count)) == 1:
            count = "0" + str(count)
        res.append(str(count))
        seconds = seconds - (metric * int(count))
    return ':'.join(res)

if __name__ == "__main__":
    x = make_readable(5)
    print(x)

