
input = open("inputs/Day4.txt", "r")

nbContained = 0

for line in input:
    line = line.replace("\n", "")

    # Creating array 1
    part1 = line.split(",")[0]
    firstStart = int(part1.split("-")[0])
    firstEnd = int(part1.split("-")[1])
    Arr1 = []
    for i in range(firstStart, firstEnd + 1):
        Arr1.append(i)
    
    # Creating array 2
    part2 = line.split(",")[1]
    secondStart = int(part2.split("-")[0])
    secondEnd = int(part2.split("-")[1])
    Arr2 = []
    for i in range(secondStart, secondEnd + 1):
        Arr2.append(i)

    contained = True

    if len(Arr1) <= len(Arr2):
        for number in Arr1:
            if number not in Arr2:
                contained = False
                break
    else:
        for number in Arr2:
            if number not in Arr1:
                contained = False
                break
    
    if contained:
        nbContained += 1


print(nbContained)


