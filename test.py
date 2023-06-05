import math

def po(num, mul):
    # rsult = math.sqrt(num)
    resultPower = 0
    result = 1
    for x in range(1, num + 1):
        # print("mult -> ",result)
        if result >= num:
            break
        else:
            resultPower += 1
            result = result * mul
        # print(resultPower)

    print(resultPower)
    print(result)
    if result == num:
        print(f"{mul} to The Power {resultPower}")
    else:
        print(f"{num} Not to the power {mul}")


#

po(16, 2)
