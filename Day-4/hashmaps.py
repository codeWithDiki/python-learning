# Hashmaps Variable

x = {
    "key1" : "Value1",
    "key2" : "Value2"
}


# Get data by key
print(x["key2"])

# Copy hashmap
y = x.copy()

y["key1"] = "Lorem"

print(x, y)

# Add Item to Hashmap 

x["key3"] = "Value3"

print(x)

# Delete item from Hashmap

del x["key3"]

print(x)

# Mixed data type dictionary

x = {
    "string" : "Value",
    "integer" : 1,
    "lists" : [1,2,3,4],
    "tuples" : (1,2,3,4),
    "dictionary" : {
        "key" : "value"
    }
}

x_list = x.get("lists")

print(len(x_list))

print(x)