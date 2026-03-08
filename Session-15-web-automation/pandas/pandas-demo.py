import pandas as pd

df= pd.read_csv("sample.csv")
print(df) # dataframe provided by pandas library
print(df.head()) # load first five data

# sorting 
print("-------------------Ascending Sort--------------------------------")
sorted_df= df.sort_values(by="price") #ascending
print(sorted_df)
print("-------------------Descending Sort--------------------------------")
sorted_df= df.sort_values(by="price",ascending=False) #descending
print(sorted_df)

print("-----------------Filtered------------------------")
filtered= df[df['price']<20]
print(filtered)

# convert filtered Data in csv 
filtered.to_csv('under_twenty.csv',index=False)
print("-----------------Average------------------")
print("Average price: ",df['price'].mean())
print("Average price: ",df['rating'].mean())