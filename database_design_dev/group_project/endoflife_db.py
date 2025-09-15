import requests
import pandas as pd

# df = pd.read_csv("endoflife_products.csv")
# print(df.shape)


products = ['iphone', 'ipad', 'apple-watch']

all_data = []

headers = {"Accept": "application/json"}

for product in products:
    print(f"Fetching data for {product}...")
    url = f"https://endoflife.date/api/{product}.json"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        for item in data:
            item['product'] = product  # add product name for reference
            all_data.append(item)
    else:
        print(f"Error fetching {product}: {response.status_code}")

df = pd.DataFrame(all_data)
print(df.head())  # prints the combined JSON response as a pandas DataFrame

df.to_csv("endoflife_products.csv", index=False)

