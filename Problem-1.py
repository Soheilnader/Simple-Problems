import random

lst = [1, 4, 5, 8, 10]
answer = lst[0] * (lst[1] - lst[2] / lst[3]) + lst[4]
guess = 0
while True:
    random.shuffle(lst)
    answer = lst[0] * (lst[1] - lst[2] / lst[3]) + lst[4]
    print (lst)
    print (answer)
    guess += 1
    if answer == 11:
        print("Number of guesses: %d" %(guess))
        break
