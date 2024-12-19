import pandas as pd

data = [
    {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    },
    {
        "name": "Jane Doe",
        "age": 25,
        "city": "Los Angeles"
    },
    {
        "name": "Bob Smith",
        "age": 40,
        "city": "Chicago"
    }
]


df = pd.DataFrame(data)

df.to_csv("data/data.csv", index=False)