import time, tracemalloc

tracemalloc.start()
start = time.time()

data = []
with open("day1.txt") as f:
    score = 0
    for line in f.readlines():
        if line == "\n":
            data.append(score)
            score = 0
        else:
            score += int(line)
data.sort()

answer1 = data[-1]
answer2 = sum(data[-3:])

print("Part 1:", answer1)
print("Part 2:", answer2)

print("Elapsed time", time.time()-start)
print("Memory usage:", tracemalloc.get_traced_memory()[0], " Peak: ", tracemalloc.get_traced_memory()[1])
tracemalloc.stop()