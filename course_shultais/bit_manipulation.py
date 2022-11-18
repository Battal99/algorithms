a = 10
b = 3
a ^= b
b ^= a
a ^= b
a >>= b
print(a)