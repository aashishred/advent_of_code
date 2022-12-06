import time, tracemalloc

tracemalloc.start()
start = time.time()

with open("day4.txt") as f:
    answer1 = 0
    answer2 = 0
    for line in f.readlines():
        sections = line.strip().split(",")
        elf1 = (sections[0].split("-"))
        elf2 = (sections[1].split("-"))

        elf1 = [x for x in range(int(elf1[0]), int(elf1[1])+1)]
        elf2 = [x for x in range(int(elf2[0]), int(elf2[1])+1)]
        
        if (all(section in elf1 for section in elf2)) or (all(section in elf2 for section in elf1)):
            answer1 += 1
        if (any(section in elf1 for section in elf2)):
            answer2 += 1

print("Part 1:", answer1)
print("Part 2:", answer2)

print("Elapsed time", time.time()-start)
print("Memory usage:", tracemalloc.get_traced_memory()[0], " Peak: ", tracemalloc.get_traced_memory()[1])
tracemalloc.stop()