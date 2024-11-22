def roman_to_integer(roman):
    roman_values = {
        'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 500, 'm': 1000,
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    for i in range(len(roman) - 1):
        currentVal = roman_values[roman[i]]
        nextVal = roman_values[roman[i + 1]]
        if currentVal < nextVal:
            total -= currentVal
        else:
            total += currentVal

    total += roman_values[roman[-1]]
    return total

while(True):
    roman_numeral = input("Enter a Roman numeral: ").strip()

    integer_value = roman_to_integer(roman_numeral)
    print(f"The integer value of '{roman_numeral.upper()}' is: {integer_value}")
    print();
