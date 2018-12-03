# https://www.codewars.com/kata/pete-the-baker/train/python

def cakes(recipe, available):
    count = 0
    for x in recipe:
        if x in available:
            amount = available[x] // recipe[x]
            if amount == 0:
                return 0
            if count == 0:
                count = amount
            elif amount < count:
                count = amount
        else:
            return 0
    return count


if __name__ == "__main__":
    print('should equal 2:')
    recipe = {"flour": 500, "sugar": 200, "eggs": 1}
    available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
    a = cakes(recipe, available)
    print(a)
    print('should equal 0:')
    recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
    available = {"sugar": 500, "flour": 2000, "milk": 2000}
    a = cakes(recipe, available)
    print(a)

