
a = [1, 2, 3, 4, 5]
results = []
for i, val in enumerate(a):
    if i % 2 == 0:
        results.append(val ** 2)
    
    else:
        results.append(val * 3)

print(results)

