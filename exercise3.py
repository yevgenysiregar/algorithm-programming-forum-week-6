stock = {

 "banana": 6,
 "apple": 0,
 "orange": 32,
 "pear": 15

}

prices = {

 "banana": 4,
 "apple": 2,
 "orange": 1.5,
 "pear": 3

}

def compute_bill(food):
    total = 0
    for i in food:
        total += food[i]
    return total

def second_compute_bill(food):
    total = 0
    for i in food:
        if stock[i] != 0:
            total += food[i]
            stock[i] -= 1
    return total

print(compute_bill(prices))
print(second_compute_bill(prices))