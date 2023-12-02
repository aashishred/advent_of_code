import time, tracemalloc

tracemalloc.start()
start = time.time()

def partOne():
    numbers = []
    with open("day1.txt") as f:
        for line in f.readlines():
            lineNumbers = [char for char in line if char.isnumeric()]
            calibrationValue = lineNumbers[0] + lineNumbers[-1]
            numbers.append(int(calibrationValue))
    return sum(numbers)      

def partTwo():
    numbers = []
    spelledNumbers = {
        "one":"on1e",
        "two":"tw2o",
        "three":"thr3ee",
        "four":"fo4ur", 
        "five":"fi5ve", 
        "six":"si6x", 
        "seven":"sev7en", 
        "eight":"eig8ht", 
        "nine":"ni9ne"
    }
    with open("day1.txt") as f:
        for line in f.readlines():
            for spelling, embeddedNumber in spelledNumbers.items():
                line = line.replace(spelling, embeddedNumber)

            lineNumbers = [char for char in line if char.isnumeric()]
            calibrationValue = lineNumbers[0] + lineNumbers[-1]
            numbers.append(int(calibrationValue))
    return sum(numbers)    



# print("Part 1:", partOne()) # 0.12 seconds
print("Part 2:", partTwo())

print("Elapsed time", time.time()-start)
print("Memory usage:", tracemalloc.get_traced_memory()[0], " Peak: ", tracemalloc.get_traced_memory()[1])
tracemalloc.stop()