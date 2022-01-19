import collections


def dicrdNonMatchValue(listData):
    partns = "xxx-xxx-xxxx"
    filterdata = []
    original_partn = []
    splitpatrn = partns.split("-")
    for partn in splitpatrn:
        lengthpartn = len(partn)
        # print(lengthpartn)
        original_partn.append(lengthpartn)
    for x in listData:
        # print(x)
        splitDatas = x.split("-")
        toBeMatch = []

        for splitData in splitDatas:
            lengthSplitData = len(splitData)
            # print(lengthSplitData)
            toBeMatch.append(lengthSplitData)

        if collections.Counter(original_partn) == collections.Counter(toBeMatch):
            print("Same")
            filterdata.append(x)
        else:
            print("No")

    return filterdata


listData = ['22x-r2x-vv33', 'ddt-fsw-xfx', 'ccx-fd-f3', 'ghx-02c-c4hh']
print(dicrdNonMatchValue(listData))
