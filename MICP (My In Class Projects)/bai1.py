a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]
ok = "True"

for i in range(len(a)-1):
    if ((a[i] > a[i-1]) and (a[i] < a[i+1])) or \
        ((a[i] < a[i-1]) and (a[i] > a[i+1])):
        ok = "False"

print(ok)
