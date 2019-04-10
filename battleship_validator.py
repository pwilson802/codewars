# https://www.codewars.com/kata/battleship-field-validator/train/python

def validate_battlefield(field):
    # Find 2 battleship, 2 cruisers, 3 destroyers, 4 submarines
    battle_key = { battleship: 4,
                   cruiser: 3,
                   destroyer: 2,
                   submarine: 1}
    while True:
        count = 0
        col_hit = 'none'
        for row_num, row in enumerate(field):
            for col_num, x in enumerate(row):
                if x == 1:
                    count += 1
                    try:






battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                 [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
