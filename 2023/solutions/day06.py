import time, tracemalloc
import numpy as np

tracemalloc.start()
start = time.time()

def partOne():
    answer = 1
    with open("day06.txt") as f:
        lines = f.readlines()
        times = [int(x) for x in lines[0].split(":")[1].split()]
        distances = [int(x) for x in lines[1].split(":")[1].split()]
        races = {time:distance for time,distance in zip(times, distances)}

    for time in times:
        waysToWin = 0
        for i in range(time+1):
            myDistance = i * (time - i)
            if myDistance > races[time]:
                waysToWin += 1
        answer *= waysToWin
    return answer
    
def partTwo():
    with open("day06.txt") as f:
        lines = f.readlines()
        time = int([lines[0].split(":")[1].replace(" ", "")][0])
        distance = int([lines[1].split(":")[1].replace(" ", "")][0])

    # waysToWin = 0
    # for i in range(0, time+1):
    #     myDistance = i * (time - i)
    #     if myDistance > distance:
    #         waysToWin += 1
    # return waysToWin

    '''
        Takes way too long; will be more efficient if we just check manually when the inequality is true.
        Let time = t, distance = d
        Want: i*(t - i) > d
        -> -i^2 + it > d
        -> -i^2 + ti - d > 0

        Then the number of solutions/ways to win is just the difference between the two roots of that quadratic.
    '''
    a = -1; b = time; c = -distance
    roots = np.roots([a, b, c])

    waysToWin = abs(np.ceil(roots[1]) - np.ceil(roots[0]))
    return int(waysToWin)

print("Part 1:", partOne())
print("Part 2:", partTwo())

print("\nElapsed time", time.time()-start)
print("Memory usage:", tracemalloc.get_traced_memory()[0], " Peak: ", tracemalloc.get_traced_memory()[1])
tracemalloc.stop()