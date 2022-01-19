# out_p = []
# finl_out = []
# for x in range(100, 1000000):
#     # if x > 1:
#     # for j in range(2, x):
#     #     if ((x % j) == 0):
#     #         break
#     # else:
#     #     out_p.append(x)
#     out_p = [j for j in range(2, x) if ((x % j) == 0)]
# out_p = [i for i in range(100, 1000000) if all((i % j) != 0 for j in range(2, i))]


# print(out_p)
# minD = min(out_p)
# maxd = max(out_p)
# finl_out.append(minD)
# finl_out.append(maxd)
# print(finl_out)


# list1 = [1, 2, [3, 4], 5, 6]
# out = []
#
#
# def checkList(listv):
#     for i in listv:
#         if type(i) != list:
#             out.append(i)
#         else:
#             checkList(i)
#
#
# a = checkList(list1)
# print(out)

# select count(emp.emp_id)
# dept.dept_name
# from mapper
# join emp on emp.emp_id=mapper.emp_id
# join dept on dept.dept_id=mapper.dept_id
# group by dept.dept_id


def primen(num):
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if (num % i) == 0:
                print("not Prime")
                break
        else:
            print("Prime")
    else:
        print("Prime")


print(primen(3))
