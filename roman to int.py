class Solution(object):
    def romanToInt(self, s):
        roman_numbers = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        sum = 0

        i = 0

        while i < len(s):
            char = s[i]
            next_char = s[i + 1] if i + 1 < len(s) else ""
            combo = char + next_char

            if combo == "IV":
                sum += 4
                i += 2
                continue
            elif combo == "IX":
                sum += 9
                i += 2
                continue
            elif combo == "XL":
                sum += 40
                i += 2
                continue
            elif combo == "XC":
                sum += 90
                i += 2
                continue
            elif combo == "CD":
                sum += 400
                i += 2
                continue
            elif combo == "CM":
                sum += 900
                i += 2
                continue

            sum += roman_numbers[char]

            i += 1

        return sum
