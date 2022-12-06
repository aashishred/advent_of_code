import time, tracemalloc

def bothParts(length):
    answer = 0
    with open("day6.txt") as f:
        data = f.readline()

        letters = [' '] * length
        for letter in data:
            answer += 1
            letters = letters[1:]
            letters.append(letter)
            if len(set(letters)) == length and letters[0] not in [' ']:
                break
    return answer

tracemalloc.start()
start = time.time()

answer1 = bothParts(4)
answer2 = bothParts(14)

print("Part 1:", answer1)
print("Part 2:", answer2)

print("Elapsed time", time.time()-start)
print("Memory usage:", tracemalloc.get_traced_memory()[0], " Peak: ", tracemalloc.get_traced_memory()[1])
tracemalloc.stop()