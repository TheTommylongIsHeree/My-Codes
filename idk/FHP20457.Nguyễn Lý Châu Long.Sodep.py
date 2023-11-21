try:
    so_str = input("so: ")
    so_int = int(so_str)
except TypeError:
    print("NaN")
    exit(1)
except ValueError:
    print("NaN")
    exit(1)

length_of_so = 0
total = 0

for i in so_str:
    length_of_so += 1
    total += int(i)

print(total % length_of_so == 0)
