# Example file for Programming Foundations: Algorithms by Joe Marini
# demonstrate dictionary usage


# TODO: create a dictionary all at once
items1 = dict({"k1": 1, "k2": 2, "k3": 3})
print(items1)

# TODO: create a dictionary progressively
items2 = {}
items2["k1"] = 1
items2["k2"] = 2
print(items2)

# TODO: replace an item
items2["k2"] = "two"

# TODO: try to access a nonexistent key
# items2["k3"]

# TODO: iterate the keys and values in the dictionary
for k, v in items2.items():
  print(f"key: {k}, value: {v}")