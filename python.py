l=[2,5,4,9,12,21,18,15]
dict=()
for i in 1:
    if i%2==0:
        dict[i]=i**2
    else:
        dict[i]=i**3
print(dict)