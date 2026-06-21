def count_kwargs(**kwargs):
    return len(kwargs)
print(count_kwargs(
    name="rahul",
    age=24,
    city="delhi"))