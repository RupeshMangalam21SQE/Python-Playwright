# 3. Merge & Deduplicate
list1, list2 = [1, 2, 3], [3, 4, 5]
merged = list(set(list1) | set(list2))
print(merged)