original_array = [2, 8, 9, 48, 8, 22, -12, 2]
result = []

for value in original_array:
    if value > 5:
        result.append(value + 2)

result_set = set(result)

print(original_array)
print(result_set)
