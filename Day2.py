
input = open("inputs/Day2.txt", "r")

TotalScore = 0


for line in input:
    match line[0]:
        case "A":
            playyed = "A"
        case "B":
            playyed = "B"  # Paper > Rock 1
        case "C":
            playyed = "C"  # Scissors > Paper 2

    match line[2]:
        case "X":
            if playyed == "A":
                # need to play scissors 3
                TotalScore += 3
            elif playyed == "B":
                # need to play rock 1
                TotalScore += 1
            elif playyed == "C":
                # need to play paper 2
                TotalScore += 2
        case "Y":
            # draw => +3
            TotalScore += 3

            if playyed == "A":
                # need to play rock 1
                TotalScore += 1
            elif playyed == "B":
                # need to play paper 2
                TotalScore += 2
            elif playyed == "C":
                # need to play scissors 3
                TotalScore += 3
        case "Z":
            # win => +6
            TotalScore += 6
            
            if playyed == "A":
                # need to play paper 2
                TotalScore += 2
            elif playyed == "B":
                # need to play scissors 3
                TotalScore += 3
            elif playyed == "C":
                # need to play rock 1
                TotalScore += 1

print(TotalScore)