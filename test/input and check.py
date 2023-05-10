class A:
    def __init__(self, number):
        self.number = number

    def add_num(self, number):
        result = 0
        for x in range(1, number + 1):
            result = result + x
        return result

    def validate_number(self, number):
        # print(number.isdigit())
        # print(number.isnumeric())
        # print(type(number))
        # print(int(number))
        number = str(number)
        if number.isnumeric():
            number = int(number)
            result1 = self.add_num(number)
            return result1
        else:
            return "Not a Number"


input_data = (input("Please enter a no :"))
calssA = A(input_data)
print("calssA :", calssA)

finalout = calssA.validate_number(input_data)
print("finalout :", finalout)
