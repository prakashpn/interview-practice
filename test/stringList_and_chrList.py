words = ['this', 'is', 'apple', 'foo', 'heat']
chars = ['a', 'x', 'y', 'm', 'i', 's', 'p', 'e', 't', 'e', 'h', 'l']

output = ['this', 'is', 'heat']


def ceckchr(wordsList, charList):
    """
    :param wordsList:
    :param charList:
    :return: if every char of string is present in chars list ,then return that string otherwise don't return
                if more than one same char is present in string ,if same no of char is present in chars list then retrun
                other wise dont
    """
    outputList = []
    for x in wordsList:
        stringchar = []

        for char in x:
            countword = x.count(char)
            countda = charList.count(char)
            if countword > countda:
                stringchar = []
                break
            if countword <= countda:
                if char in charList:
                    stringchar.append(char)
        stringcharjoin = "".join(stringchar)
        if stringcharjoin:
            outputList.append(stringcharjoin)

    return outputList


a = ceckchr(words, chars)
print("Final OutPut : ", a)
