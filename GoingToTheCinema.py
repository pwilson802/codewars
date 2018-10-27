def movie(card, ticket, perc):
    b_cost = card
    my_try = 1
    new_ticket = ticket * perc
    while True:
        a_cost = my_try * ticket
        new_ticket = new_ticket * perc
        b_cost += new_ticket
        if b_cost < a_cost:
            return my_try
        my_try += 1

if __name__ == '__main__':
    x = movie(50000000, 15, 0.9)
    print(x)