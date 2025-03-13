def to_number(roman):
    numbers = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    
    total = 0
    length = len(roman)

    for i in range(length-1):
        if (numbers[roman[i]] < numbers[roman[i+1]]):
            total -= numbers[roman[i]]
        else:
            total += numbers[roman[i]]

    total += numbers[roman[length-1]]
    return "Converted to: " + total

print(to_number("MCMVII"))

