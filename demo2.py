a = {'Nikhil': {'English': 5, 'Maths': 2, 'Science': 14},
     'Akash': {'English': 15, 'Maths': 7, 'Science': 2},
     'Akshat': {'English': 5, 'Maths': 50, 'Science': 20}}
# print()

las=[]
for x in a.items():
    out = sorted(a.items(), reverse=True)
    print(out)
