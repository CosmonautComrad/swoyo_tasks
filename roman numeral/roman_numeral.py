def roman_numerals_to_int(roman_numeral):

    if not isinstance(roman_numeral, str):
        return None

    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    for symb in roman_numeral:
        if symb not in roman.keys():
            return None

    arabic = roman.get(roman_numeral)

    if arabic is not None:
        return arabic

    else:
        arabic = 0
        for i in range(len(roman_numeral)):

            if i < len(roman_numeral) - 1 and roman[roman_numeral[i]] < roman[roman_numeral[i + 1]]:
                arabic -= roman[roman_numeral[i]]
            else:
                arabic += roman[roman_numeral[i]]

        return arabic


print(roman_numerals_to_int('MMMMCXXIX'))
