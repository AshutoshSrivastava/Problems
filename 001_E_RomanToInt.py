def romanToInt(s: str) -> int:
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total_value = 0
    prev_value = 0
    for char in reversed(s):
        value = roman_map[char]
        if value < prev_value:
            total_value -= value
        else:
            total_value += value
        prev_value = value
    return total_value

# Example usage:
if __name__ == "__main__":
    print(romanToInt("III"))      # Output: 3
    print(romanToInt("IV"))       # Output: 4
    print(romanToInt("IX"))       # Output: 9
    print(romanToInt("LVIII"))    # Output: 58
    print(romanToInt("MCMXCIV"))  # Output: 1994