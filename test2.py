# # class s:
# #     x=1
# # class a(s):
# #     pass
# # class b(s):
# #     pass
# # print(s.x,a.x,b.x)
# # a.x=2
# # print(s.x,a.x,b.x)
# import collections
#
#
# def sol(s):
#     count=collections.Counter(s)
#     print(count)
#     for x,i in enumerate(s):
#         if count[i]==1:
#             return x
#     return -1
# print(sol("alphabate"))
# print(sol("barbados"))
# print(sol("crunchy"))




def mu():
    return [lambda x:i*x for i in range(4)]

print([m(2) for m in mu()])







