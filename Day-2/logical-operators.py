# And Operator

x = 10
x2 = 10

y = 5
y2 = 5

z = x == x2 # True
z2 = y == y2 # True

print(f"Hasil logical dari x and y : {z and z2}")

# Or Operator

x = 10
x2 = 10

y = 5
y2 = 5

z = x == x2 # True
z2 = y != y2 # False

print(f"Hasil logical dari x or y : {z or z2}")

# Not Operator

x = 10
x2 = 10

y = 5
y2 = 5

z = x != x2 # True

print(f"Hasil logical dari x not y : {not z}")


# Gabungan And, Or Not

x = 10
x2 = 10

y = 5
y2 = 5

z = x == x2 # True
z2 = y == y2 # True

hasil = (z and z2) or not z

print(f"Hasil penggabungan And, Or, Not : {hasil}")