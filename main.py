import random
rand_num = random.randrange(1, 51)
counter = 0
pile = []
maxtry = 5
prediction = 0

while prediction != rand_num:
    counter += 1
    prediction = int(input("Write an integer between 0 and 51: "))

    pile.append(prediction)

    if prediction < 1 or prediction > 50:

        print("INVALID NUMBER Please write an integer between 0 and 51")

        counter += -1

    elif counter > 5:

        print("YOU LOST"
              ""
              " THE NUMBER WAS {}.".format(rand_num))

        print("You predicted those numbers", pile)

        break

    elif rand_num > prediction:
        print("Please choose a bigger number")

    elif rand_num < prediction:
        print("Please choose a smaller number")

    else:
        print("YOU WIN AT YOUR {}. TRY".format(counter))

        print("You predicted those numbers", pile)
        break
