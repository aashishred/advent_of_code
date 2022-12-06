#A = Rock, B = Paper, C = Scissors
#X = Rock, Y = Paper, Z = Scissors
import time, tracemalloc

tracemalloc.start()
start = time.time()

def partOne():
    choicescore = 0
    resultscore = 0

    with open("day2.txt") as f:
        lines = f.readlines()
        for line in lines:
            me = line[2]
            them = line[0]

            if me == "X":
                choicescore += 1
            elif me == "Y":
                choicescore += 2
            elif me == "Z":
                choicescore += 3
            
            if (me == "X" and them == "A") or (me == "Y" and them == "B") or (me == "Z" and them == "C"):
                resultscore += 3
            elif (me == "X" and them == "C") or (me == "Y" and them == "A") or (me == "Z" and them == "B"):
                    resultscore += 6
    answer1 = choicescore + resultscore
    return answer1

def partTwo():
    score = 0
    with open("day2.txt") as f:
        lines = f.readlines()
        for line in lines:
            them = line[0]
            result = line[2]
            if them == "A" and result == "X":
                score += 3
            elif them == "A" and result == "Y":
                score += 4
            elif them == "A" and result == "Z":
                score += 8
            if them == "B" and result == "X":
                score += 1
            elif them == "B" and result == "Y":
                score += 5
            elif them == "B" and result == "Z":
                score += 9
            if them == "C" and result == "X":
                score += 2
            elif them == "C" and result == "Y":
                score += 6
            elif them == "C" and result == "Z":
                score += 7
    return score

print("Part 1:", partOne())
print("Part 2:", partTwo())

print("Elapsed time", time.time()-start)
print("Memory usage:", tracemalloc.get_traced_memory()[0], " Peak: ", tracemalloc.get_traced_memory()[1])
tracemalloc.stop()