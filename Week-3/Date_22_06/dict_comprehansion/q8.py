# 30.	Create a dictionary from two lists:
keys = ["name", "age", "city"]
values = ["Monika", 18, "Ratlam"]

new_dict={keys[i]:values[i] for i in range(len(keys))}

print(new_dict)