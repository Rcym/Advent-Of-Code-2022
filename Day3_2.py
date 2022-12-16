input = open("inputs/Day3.txt", "r")

priority = 0
group = []

prioDico = {
    "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26,
    "A": 27, "B": 28, "C": 29, "D": 30, "E": 31, "F": 32, "G": 33, "H": 34, "I": 35, "J": 36, "K": 37, "L": 38, "M": 39, "N": 40, "O": 41, "P": 42, "Q": 43, "R": 44, "S": 45, "T": 46, "U": 47, "V": 48, "W": 49, "X": 50, "Y": 51, "Z": 52
}

for line in input:
    line = line.replace("\n", "")
    group.append(line)

    if len(group) == 3:
        comp1 = group[0]
        comp2 = group[1]
        comp3 = group[2]
        found = False

        for i in range(0, len(comp1)):
            for j in range(0, len(comp2)):
                for k in range(0, len(comp3)):
                    if comp1[i] == comp2[j] == comp3[k]:
                        priority += prioDico[comp1[i]]
                        print(comp1[i], comp2[j], comp3[k], prioDico[comp1[i]])
                        found = True
                        break
                if found:
                    break
            if found:
                break
        group = []

print(priority)
