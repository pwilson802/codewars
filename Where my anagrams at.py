#vhttps://www.codewars.com/kata/where-my-anagrams-at/train/python

def anagrams(word, words):
    return [x for x in words if sorted(x) == sorted(word)]


a = anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])
print(a)

# Test.assert_equals(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])