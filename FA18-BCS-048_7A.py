# Reading Table
tableFile = open("table.txt", "r") 
tableLines = tableFile.readlines()
tableHeader = []

for word in tableLines[0].rstrip().split(' '):
    afterRemoving = word.rstrip().split('\t')
    for newWord in afterRemoving:
        if newWord == '':
            continue
        tableHeader.append(newWord)

print('Table Header:', tableHeader)

fullTable = []

for index, line in enumerate(tableLines):
    if index == 0: # Skipping Header
        fullTable.append(tableHeader)
        continue
    
    fullTable.append(line.rstrip().split('\t'))
    print('Table Line: ', line.rstrip().split('\t'))
    

# Reading Input
inputFile = open('input.txt', 'r')
startingInput = []
readFile = inputFile.read()
inputData = readFile.split(' ')

# Tokenization
for word in inputData:
    if word in tableHeader:
        startingInput.append(word)
        print('Token Found:', word)

startingInput.append('$')

print('\nInput List After Tokenization: ', startingInput)

# Reading Grammer From File!
file = open("grammar.txt", "r")  # grammar
grammer = file.readlines()


productions = {} # {1: {left: 's', right: ['asd']}}
for index, production in enumerate(grammer):
    if (index == 0):
        continue
    rightSide = production.rstrip().split('->')[1].rstrip().split(' ') # ['chased', 'a']
    leftSide = production.rstrip().split('->')[0].rstrip().split(' ')[0] # string
    productions[f"{index}"] = { 'left': leftSide, 'right': rightSide }

print('\nProductions: ', productions, '\n')

# Now initializing Stack
stack = ['$', '0']
currentInputIndex = 0

while True:

    if len(startingInput) == 0:
        print('Parsing Failed because nothing is in Input!!!')

    stackTopElement = stack[-1]
    tableRowIndex = 1 # Default Value
    for index, row in enumerate(fullTable):
        if row[0] == stackTopElement:
            tableRowIndex = index

    tableColIndex = 1 # Default Value
    for index, word in enumerate(tableHeader):
        if startingInput[currentInputIndex] == word:
            tableColIndex = index

    operation = fullTable[tableRowIndex][tableColIndex]

    print('State: ', fullTable[tableRowIndex][0], '| Table Header: ', tableHeader[tableColIndex])

    if operation == '-':
        print('Parsed Failed!!!')
        break
    
    elif operation == "acc":
        print('Parsed Successfully')
        break

    elif operation.startswith("s"):
        print("Shift Operation:", operation)
        stack.append(startingInput[currentInputIndex])
        stack.append(operation[1:])
        currentInputIndex+=1 # Moving Forward in Input

    elif operation.startswith("r"):
        print("Reduction Operation", operation)
        reduceEquation = operation[1:]
        rightSideLength = len(productions[reduceEquation]['right']) * 2
        for _ in range(rightSideLength):
            stack.pop()

        leftSide = productions[reduceEquation]['left']
        stack.append(leftSide)

        headerElement = leftSide
        rowElement = stack[-2]

        rowIndex = 1 # Default Value
        for index, row in enumerate(fullTable):
            if row[0] == rowElement:
                rowIndex = index

        colIndex = 1 # Default Value
        for index, word in enumerate(tableHeader):
            if headerElement == word:
                colIndex = index

        stackTopTwoResult = fullTable[rowIndex][colIndex]
        stack.append(stackTopTwoResult)

    print(stack)
    print("End\n")