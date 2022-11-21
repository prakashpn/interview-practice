import json
import re

import pandas as pd

file_data = pd.read_excel("testt.xlsx", sheet_name="Sheet2")
print(file_data)
# print(file_data.get("emaiadd"))
print("-----------------------------")

file_data = file_data.to_json(orient='records')
file_data = json.loads(file_data)
print(file_data)
print(file_data[0])
print("-----------------------------")
for x in file_data:
    print(x.get("emaiadd"))
    emaiadd = x.get("emaiadd")
    splitEmail = emaiadd.split(",")
    print("splitEmail : ", splitEmail)
    # email = ""
    for email in splitEmail:
        # print(email)
        # searchData = re.search("@hdfc.com$", email)
        searchData = re.findall("hdfc.com", email)
        print(" searchData : ", searchData)
        if searchData:
            print("email :", email)
            x["hdfc"] = email

print("file_data :", file_data)
print("file_data :", file_data[2])
df_data = pd.DataFrame(file_data)
print(df_data)
df_data.to_excel("final_data.xlsx")
