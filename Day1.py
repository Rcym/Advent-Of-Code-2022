
input = open("inputs/Day1.txt", "r")
maxValue1 = 0
maxValue2 = 0
maxValue3 = 0
total = 0

for line in input:
    if line == "\n":
        if total > maxValue1:
            maxValue3 = maxValue2
            maxValue2 = maxValue1
            maxValue1 = total
        elif total > maxValue2:
            maxValue3 = maxValue2
            maxValue2 = total
        elif total > maxValue3:
            maxValue3 = total

        total = 0  
    else:
        total += int(line)



print(maxValue1)
print(maxValue2)
print(maxValue3)

print("\n")

print(maxValue1 + maxValue2 + maxValue3)