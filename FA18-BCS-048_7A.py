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
    rightSide = production.rstrip().split('->')[1].rstrip().split(' ') # ['chased', 'a']
    leftSide = production.rstrip().split('->')[0].rstrip().split(' ')[0] # string
    productions[index + 1] = { 'left': leftSide, 'right': rightSide }

print('\nProductions: ', productions)

# Now initializing Stack
stack = ['$', '0']

# while inputLoop < len(input):

#     char = input[inputLoop]
#     index_R = all_states.index(stack[-1])
#     index_C = table[0].index(char)
#     accept_state = table[index_R][index_C]

#     if accept_state == "acc":
#         print("\n")
#         print("Parsed Successfully")
#         break

#     elif accept_state.startswith("s"):

#         temp = accept_state[1:]
#         stack.append(char)
#         print(f"Current Char == {char}\What pushed in Stack Just: \n{stack}")
#         stack.append(temp)
#         print(f"Current Char == {char}\nWhat pushed in Stack Just : \n{stack}")
        

#     elif accept_state.startswith("r"):
#         temp = accept_state[1:]
#         len_grammar = 0
#         for grammar in productions.items():
#             if temp == grammar[0]:
#                 push_symbol = grammar[1].split("->")[0]
#                 temp_grammar = grammar[1].split("->")[-1]
#                 len_grammar = len(temp_grammar)
#                 break
#         for i in range(len_grammar * 2):
#             stack.pop()
#             print(f"Current Char ==> {char}\Pop Action : \n{stack}")
#         stack.append(push_symbol)
#         print(f"Current Char ==> {char}\nStack Action Push : \n{stack}")
#         temp_index_R = all_states.index(stack[-2])
#         temp_index_C = table[0].index(stack[-1])
#         temp_accept_state = table[temp_index_R][temp_index_C]
#         stack.append(temp_accept_state)
#         print(f"Charater-> {char}\Push in Stack: \n{stack}")

#     elif accept_state == "-":
#         print("\n!!Parse Failed")
#         break
#     inputLoop +=1
