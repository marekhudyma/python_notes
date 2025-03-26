my_dict = {"key1": "value1", "key2": "value2"}
print(my_dict)
print(my_dict["key1"])

price_lookup = {'apple': 2.99, "orange": 3.99}

d = {"k1": 123, "k2": [0, 1,2], "k3": {"insideKey": 100}}
print(d["k2"])
print(d["k3"]["insideKey"])

d = {"key1": ["a", "b", "c"]}
print(d["key1"][2].upper())
print(d)

d["key2"] = 200
print(d)

d["key2"] = "new value"
print(d)

print(d.keys())
print(d.values())
print(d.items())

