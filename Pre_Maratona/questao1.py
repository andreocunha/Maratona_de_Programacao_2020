c = int(input())
a = int(input())

res = (a//(c-1))
resto =  a%(c-1)
if resto > 0:
    res += 1
print(res)