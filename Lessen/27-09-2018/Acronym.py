def acronym(sentence):
    words = sentence.split(" ")
    res = ''
    for w in words:
        res += w[0].upper()
    return res

def grid(numberList):
    for i in range(len(numberList)):
        for j in range(len(numberList[i])):
            print(numberList[i][j], end=" ")
        print()

numberList = [[1,2,3,4],
             [5,6,7,8],
             [9,10,11,12],
             [13,14,15,16]]

print(grid(numberList))

print(acronym(input("Sentence: ")))