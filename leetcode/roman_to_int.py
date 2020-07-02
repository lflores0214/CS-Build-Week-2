def romanToInt(s):
    roman_to_int = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    total = 0
    i = 0
    while i < len(s) - 1:
        current = roman_to_int[s[i]]
        nxt = roman_to_int[s[i + 1]]

        if current >= nxt:
            if i == len(s) - 2:
                total += current
                total += nxt
                return total
            total += current
            i += 1
        else:
            if i == len(s) - 3:
                total += (nxt - current)
                return total
            total += (nxt - current)
            i += 2


print(romanToInt("MDCXCV"))
