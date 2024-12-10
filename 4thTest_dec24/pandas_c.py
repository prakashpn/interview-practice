# import pandas as pd
# df = pd.DataFrame({"1": [1,1,3,3,5], "2": [1,2,3,4,5]})
# # Output = {"1":[1,3,5], "3":[3,7,5]}

import pandas as pd

# Original DataFrame
df = pd.DataFrame({"1": [1, 1, 3, 3, 5], "2": [1, 2, 3, 4, 5]})

# Group by column "1" and sum column "2"
result = df.groupby("1", as_index=False).sum()

# Rename the columns to match the desired output
result.columns = ["1", "3"]

# Convert the DataFrame to the specified format
result_dict = result.to_dict(orient="list")

print(result_dict)