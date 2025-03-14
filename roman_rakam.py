class RomanToNumber:
    def __init__(self, roman: str):
        self.roman = roman.upper()
        self.numbers = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
    
    # Geçerli Roma rakamları içerip içermediğini kontrol eden fonksiyon.
    def is_valid_roman(self):
        return all(char in self.numbers for char in self.roman)
    
    # Roma rakamını 10'luk sisteme çevirir.
    def to_number(self):
        # Roma rakamlarını kontrolün gerçekleştiği kod.
        if not self.is_valid_roman():
            raise ValueError("Geçersiz Roma rakamı girdiniz!")

        total = 0
        length = len(self.roman)

        for i in range(length - 1):
            if self.numbers[self.roman[i]] < self.numbers[self.roman[i + 1]]:
                total -= self.numbers[self.roman[i]]
            else:
                total += self.numbers[self.roman[i]]

        total += self.numbers[self.roman[length - 1]]
        return total


# Kullanıcıdan giriş alma
user_input = input("Enter a Roman numeral: ").strip()

# Kullanım
try:
    roman_number = RomanToNumber(user_input)
    print(f"Converted to: {roman_number.to_number()}")
except ValueError as e:
    print(e)
