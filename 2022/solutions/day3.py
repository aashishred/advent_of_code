import time, tracemalloc

def partOne():
    with open("day3.txt") as f:
        answer1 = 0

        rucksack = []
        for line in f.readlines():
            rucksack.append(line.strip())
        for item in rucksack:
            comp1 = []
            comp2 = []

            number = len(item)
            if number % 2 == 0:
                comp1.append(item[0:number//2])
                comp2.append(item[number//2:])
            else:
                comp1.append(item[0:(number//2)+1])
                comp2.append(item[(number//2)+1:])
            
            comp1 = [letter for letter in comp1[0]]
            comp2 = [letter for letter in comp2[0]]

            priority = set([letter for letter in comp1 if letter in comp2])
            
            for letter in priority:
                if letter.lower() == letter:
                    answer1 += sum(ord(x)-96 for x in priority)
                else:
                    answer1 += sum(ord(x)-38 for x in priority)
    return answer1
    
def partTwo():
    answer2 = 0
    with open("day3.txt") as f:
        lines = [line.strip().split("\n") for line in f]
        size = len(lines)

        for i in range(size//3):
            firsts = sorted(lines[i*3])
            first = []
            [first.append(x) for x in firsts if x not in first]

            seconds = sorted(lines[(3*i)+1])
            second = []
            [second.append(x) for x in seconds if x not in second]

            thirds = sorted(lines[(3*i)+2])
            third = []
            [third.append(x) for x in thirds if x not in third]

            for letter in set(first[0]):
                if (letter in second[0]) and (letter in third[0]):
                    if letter.lower() == letter:
                        answer2 += (ord(letter)-96)
                    else:
                        answer2 += (ord(letter)-38)
    return answer2

tracemalloc.start()
start = time.time()

print("Part 1:", partOne())
print("Part 2:", partTwo())

print("Elapsed time", time.time()-start)
print("Memory usage:", tracemalloc.get_traced_memory()[0], " Peak: ", tracemalloc.get_traced_memory()[1])
tracemalloc.stop()



