import time, tracemalloc

tracemalloc.start()
start = time.time()

def partOne():
    points = 0
    with open("day04.txt") as f:
        cards = f.read().split("\n")
        for card in cards:
            card = card.split(":")[1]

            numbers = card.split("|")
            winningNumbers = [int(x) for x in numbers[0].split()]
            myNumbers = [int(x) for x in numbers[1].split()]
            
            matches = sum(1 for number in myNumbers if number in winningNumbers)
            if matches != 0:
                points += 2**(matches-1)

    return points

def partTwo():
    with open("day04.txt") as f:
        cards = f.read().split("\n")
        cardCopies = {x+1:1 for x in range(len(cards))}

        cardNumber = 0
        for card in cards:
            cardNumber += 1
            card = card.split(":")[1]

            numbers = card.split("|")
            winningNumbers = [int(x) for x in numbers[0].split()]
            myNumbers = [int(x) for x in numbers[1].split()]
            
            matches = sum(1 for number in myNumbers if number in winningNumbers)

            for i in range(1, matches+1):
                cardCopies[cardNumber + i] += cardCopies[cardNumber]

    return sum(cardCopies.values())

print("Part 1:", partOne())
print("Part 2:", partTwo())

print("\nElapsed time", time.time()-start)
print("Memory usage:", tracemalloc.get_traced_memory()[0], " Peak: ", tracemalloc.get_traced_memory()[1])
tracemalloc.stop()