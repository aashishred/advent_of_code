import time, tracemalloc
import re

tracemalloc.start()
start = time.time()

def partOne():
    with open("day02.txt") as f:
        possibleGames = []

        reds = r'\b(1[3-9]|[2-9][0-9]) red\b'
        greens = r'\b(1[4-9]|[2-9][0-9]) green\b'
        blues = r'\b(1[5-9]|[2-9][0-9]) blue\b'

        gameNumber = 0
        for game in f.readlines():
            gameNumber += 1

            redSearch = re.search(reds, game)
            greenSearch = re.search(greens, game)
            blueSearch = re.search(blues, game)
            
            if all(searches is None for searches in [redSearch, greenSearch, blueSearch]):
                possibleGames.append(gameNumber)
                
    return sum(possibleGames)

def partTwo():
    answer = 0
    with open("day02.txt") as f:
        games = f.readlines()
        for game in games:
            minRed = max(int(match) for match in re.findall(r'(\d+) red', game))
            minGreen = max(int(match) for match in re.findall(r'(\d+) green', game))
            minBlue = max(int(match) for match in re.findall(r'(\d+) blue', game))

            power = minRed * minGreen * minBlue
            answer += power
    return answer  

print("Part 1:", partOne())
print("Part 2:", partTwo())

print("Elapsed time", time.time()-start)
print("Memory usage:", tracemalloc.get_traced_memory()[0], " Peak: ", tracemalloc.get_traced_memory()[1])
tracemalloc.stop()
