size = int(input("Enter the size of the array: "))
arr = [0.0] * size
print("Enter the elements of the array:")
for j in range(size):
    arr[j] = float(input())
try:
        idx_to_access = int(input("Enter the index of the element to print: "))
        print(f"Element at index {idx_to_access}: {arr[idx_to_access]:.2f}")
except IndexError:
    print(f"Index {idx_to_access} is invalid.")