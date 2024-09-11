set1 = {8,16,24,32,44}
set2 = {7,14,8,32,21}

print("-"*50)
print(f"SET 1: {set1}")
print(f"SET 2: {set2}")
print("-"*50)
print(f"Set Difference: {set1.difference(set2)}")
print(f"Union of Set: {set1.union(set2)} ")
print(f"Symmetric Difference:{set1.symmetric_difference(set2)} ")
print(f"Set Intersection: {set1.intersection(set2)}")