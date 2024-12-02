import time, tracemalloc

tracemalloc.start()
start = time.time()

answer1 = 0
answer2 = 0
with open("day02.txt") as f:
    reports = [[int(num) for num in line.split()] for line in f]

def check_if_a_report_is_safe(input_list):
    size = len(input_list)

    if (input_list[1] > input_list[0]) and any(input_list[i + 1] < input_list[i] for i in range(size - 1)):
        return False

    if (input_list[1] < input_list[0]) and any(input_list[i + 1] > input_list[i] for i in range(size - 1)):
        return False

    for i in range(size - 1):
        if abs(input_list[i + 1] - input_list[i]) not in [1,2,3]:
            return False
    return True

for report in reports:
    if check_if_a_report_is_safe(report) == True:
        answer1 += 1
        answer2 += 1
    else:
        for i in range(len(report)):
            synthetic_report = report[:i] + report[i + 1:]
            if check_if_a_report_is_safe(synthetic_report) == True:
                answer2 += 1
                break

print("Part 1:", answer1)
print("Part 2:", answer2)

print("Elapsed time", time.time()-start)
print("Memory usage:", tracemalloc.get_traced_memory()[0], " Peak: ", tracemalloc.get_traced_memory()[1])
tracemalloc.stop()