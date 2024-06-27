class Solution:
    sub_twenty = {
        0: "",
        1: " One",
        2: " Two",
        3: " Three",
        4: " Four",
        5: " Five",
        6: " Six",
        7: " Seven",
        8: " Eight",
        9: " Nine",
        10: " Ten",
        11: " Eleven",
        12: " Twelve",
        13: " Thirteen",
        14: " Fourteen",
        15: " Fifteen",
        16: " Sixteen",
        17: " Seventeen",
        18: " Eighteen",
        19: " Nineteen",
    }

    tens = {
        2: " Twenty",
        3: " Thirty",
        4: " Forty",
        5: " Fifty",
        6: " Sixty",
        7: " Seventy",
        8: " Eighty",
        9: " Ninety",
    }

    def hundreds(self, to_convert: int) -> str:
        if to_convert == 0:
            return ""
        result = ""

        # Hundreds
        hundreds = to_convert // 100
        print(hundreds)
        if hundreds > 0:
            result = result + self.sub_twenty[hundreds] + " Hundred"

        # Tens
        to_convert = to_convert - (hundreds * 100)
        tens = to_convert // 10
        print(tens)
        if to_convert < 20:
            result = result + self.sub_twenty[to_convert]
        else:
            if tens > 0:
                result = result + self.tens[tens]
            
            # Ones
            to_convert = to_convert - (tens * 10)
            ones = to_convert // 1
            print(ones)
            if ones > 0:
                result = result + self.sub_twenty[ones]
                
        return result

    def numberToWords(self, num: int) -> str:
        # 1. Simulate how we read the numbers
        #    Notice that we read three digits as a number, then add suffix (billion, million, thousand)
        # 2. In the sub hundreds accuracy, we can break it down:
        #    Hundreds are read as: "x hundred"
        #    Tens are red as: "Twenty, Thirty, Fourty, etc..." with exception being if its a 1, then we have another map from 0 ... 19 with specific words
        #    Ones are red simply as the number
        # 3. We need to get the digits of the number then have a map that maps them to the english

        # Define mappings

        if num == 0:
            return "Zero"

        billions = num // 1000000000
        print(billions)
        num -= (billions * 1000000000)

        millions = num // 1000000
        print(millions)
        num -= (millions * 1000000)
        
        thousands = num // 1000
        print(thousands)
        num -= (thousands * 1000)

        # Build string result
        result = ""
        if billions > 0:
            result += self.hundreds(billions) + " Billion"
        if millions > 0:
            result += self.hundreds(millions) + " Million"
        if thousands > 0:
            result += self.hundreds(thousands) + " Thousand"
        result += self.hundreds(num)

        # Remove white space at end of string if there is
        if result[-1] == " ":
            result = result[:-1]
        if result[0] == " ":
            result = result[1:]
        print(result)

        return result
