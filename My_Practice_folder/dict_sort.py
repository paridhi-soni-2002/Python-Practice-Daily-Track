value={
    "Riya":85,"Aman":92,"John":78,"Bob":88
    }

result=dict(sorted(value.items(),key=lambda x:x[1]))
print(result)