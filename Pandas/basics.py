import pandas as pd
data = {
    'name' : ['Shozab', 'Faaz', 'Ali', 'Hassan', 'Adeel'],
    'age' : [20, 21, 19, 18, 22],
    'gpa' : [3.9, 3.5, 3.7, 3.8, 3.6]
}

#Series – A one-dimensional labeled array.
#DataFrame – A two-dimensional labeled table.

df = pd.DataFrame(data)
ds = pd.Series(data['age']).tolist()
print(ds)