a = [1, 2, 3, 4]
print("inputs", a)

n = len(a)
outputs = [0] * n

l_product = 1
for idx in range(n):
    outputs[idx] = l_product
    l_product *= a[idx]
    
print("first_pass", outputs)

r_product = 1
for idx in range(n - 1, -1, -1):
    outputs[idx] *= r_product
    r_product *= a[idx]

print("second_pass", outputs)
