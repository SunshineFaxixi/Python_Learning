

even_total = 0
for num in range(2, 101, 2):
    even_total += num

print(even_total)

even_total1 = 0
for num in range(1, 101, 1):
    if num % 2 == 0:
        even_total1 += num

print(even_total1)