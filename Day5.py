
input = open("inputs/Day5.txt", "r")

stack1 = ["Z", "T", "F", "R", "W", "J", "G"]
stack2 = ["G", "W", "M"]
stack3 = ["J", "N", "H", "G"]
stack4 = ["J", "R", "C", "N", "W"]
stack5 = ["W", "F", "S", "B", "G", "Q", "V", "M"]
stack6 = ["S", "R", "T", "D", "V", "W", "C"]
stack7 = ["H", "B", "N", "C", "D", "Z", "G", "V"]
stack8 = ["S", "J", "N", "M", "G", "C"]
stack9 = ["G", "P", "N", "W", "C", "J", "D", "L"]

result = ""

stacks = [stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

def Move(nbToMove, fromStack, toStack):
    for i in range(nbToMove):
        package = stacks[fromStack-1].pop()
        stacks[toStack-1].append(package)

def Moove(nbToMove, fromStack_e, toStack_e):
    fromStack = stacks[fromStack_e-1]
    toStack = stacks[toStack_e-1]

    # getting all the packages fromStack
    crates = []
    for i in range(nbToMove):
        crates.append(fromStack.pop())
    # keeping the same order as they were
    crates.reverse()

    # Moving crates in toStack
    for i in range(nbToMove):
        toStack.append(crates[i])




for line in input:
    line = line.replace("move ","")
    line = line.replace(" from ",",")
    line = line.replace(" to ",",")
    line = line.replace("\n","")

    line = line.split(",")
    nbToMove = int(line[0])
    fromStack = int(line[1])
    toStack = int(line[2])

    Moove(nbToMove, fromStack, toStack)


for i in range(len(stacks)):
    print(stacks[i])
    theStack = stacks[i]
    lastCrate = len(theStack)-1
    
    result += theStack[lastCrate]

print(result)


