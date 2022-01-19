class calculatr:
    sumadd = 0

    def __init__(self):
        # self.a = a
        # self.b = b
        self.sumadd = 0

    def add(self, *args):
        for a in args:
            self.sumadd = self.sumadd + a
        return self.sumadd

    # def averageNum(listData):


#     newList = []
#     try:
#         for x in listData:
#             if isinstance(x, int):
#                 newList.append(x)
#         return sum(newList) / len(newList)
#     except:
#         print("u have put string")


Lio = [12, 10, 13, 14]
# print(averageNum(Lio))
callD = calculatr()

callD1 = callD.add(1, 2)
callD2 = callD.add(14)
print(callD2)
# print(callD1)
