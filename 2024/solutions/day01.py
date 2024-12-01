import time, tracemalloc

tracemalloc.start()
start = time.time()

left_list = []
right_list = []
with open("day01.txt") as f:
    for line in f:
        left, right = line.strip().split()
        left_list.append(int(left))
        right_list.append(int(right))

left_list, right_list = sorted(left_list), sorted(right_list)

answer1 = 0
for i in range(len(left_list)):
    answer1 += abs(left_list[i] - right_list[i])

answer2 = 0
for i in left_list:
    occurences_of_i = sum(1 for x in right_list if x == i)
    answer2 += i * occurences_of_i


print("Part 1:", answer1)
print("Part 2:", answer2)

print("Elapsed time", time.time()-start)
print("Memory usage:", tracemalloc.get_traced_memory()[0], " Peak: ", tracemalloc.get_traced_memory()[1])
tracemalloc.stop()