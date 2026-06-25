def unique(num):
    seen=set()
    for i in num:
        if i not in seen:
            seen.add(i)
            yield i
            
print(list(unique([1,1,12,23,12,34])))