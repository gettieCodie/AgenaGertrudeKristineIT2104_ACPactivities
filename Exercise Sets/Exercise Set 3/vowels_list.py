name = list(input("Enter a String: "))
VOWELS = ['a','e','i','o','u','A','E','I','O','U']
vowelList = []

for search in name:
    if search in VOWELS:
        vowelList.append(search)

print(vowelList)
