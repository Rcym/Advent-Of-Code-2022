
input = open("inputs/Day2.txt", "r")

TotalScore = 0


for line in input:
    match line[0]:
        case "A":
            playyed = "A"
        case "B":
            playyed = "B"
        case "C":
            playyed = "C"

    match line[2]:
        case "X":
            TotalScore += 1
            if playyed == "A": # respond rock to rock
                TotalScore += 3
            elif playyed == "C": # respond rock to cissors
                TotalScore += 6
        case "Y":
            TotalScore += 2
            if playyed == "B":
                TotalScore += 3
            elif playyed == "A":
                TotalScore += 6
        case "Z":
            TotalScore += 3
            if playyed == "C":
                TotalScore += 3
            elif playyed == "B":
                TotalScore += 6

print(TotalScore)