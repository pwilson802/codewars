# https://www.codewars.com/kata/dubstep/train/python

def song_decoder(song):
    return ' '.join(song.replace('WUB', ' ').split())


if __name__ == "__main__":
    x = song_decoder("AWUBBWUBC")
    i = song_decoder("AWUBWUBWUBBWUBWUBWUBC")
    print(x)
    print(i)