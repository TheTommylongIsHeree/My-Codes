cac_so = []
try:
    for i in range(10):
        so_str = input("so: ")
        so_int = int(so_str)
        cac_so.append(so_int)
except TypeError:
    print("NaN")
    exit(1)
except ValueError:
    print("NaN")
    exit(1)

so_cant_be_devided = []

for so in cac_so:
    so_can_be_devided = False
    for i in range(1, so):
        if so % i == 0:
            so_can_be_devided = True
    if (not so_can_be_devided):
        so_cant_be_devided.append(so)

print("Các số nguyên tố là:")
for i in so_cant_be_devided:
    print(i)

exit(0)
