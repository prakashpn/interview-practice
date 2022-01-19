# “””
# Heuristics for priority:
# * Exact matches first
# * when query is a separate word (lower index match first if multiple)
# * Results that have the search string (lower index match first if multiple)
# * skip the rest
# “””
import re

key = 'word'
results = ['1Password',
           'wordperfect',
           'aword',
           'Does this have what you want?',
           'Microsoft word',
           'word',
           'yet another word',
           'this does not have what you want']


def findWord(search, listData):
    outputList = []
    for actualSearch in listData:
        if search == actualSearch:
            outputList.append(actualSearch)
    for separMatch in listData:
        splitList = separMatch.split(" ")
        # print(splitList)
        if (len(splitList) > 1):
            if search in splitList:
                outputList.append(separMatch)

    exceptList = []
    for it in listData:
        if it not in outputList:
            exceptList.append(it)
    # print("exceptList ", exceptList)

    out = list(filter(lambda x: search in x, exceptList))

    outputList.extend(out)

    return outputList


response = findWord(key, results)
print(response)
