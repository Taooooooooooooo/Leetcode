import re


class Solution:
    def myAtoi(self, s: str) -> int:
        stripS = s.strip()
        if stripS == '' or stripS == '+' or stripS == '-':
            return 0
        if stripS[0].isdigit():
            result = int(re.search(r"(\d+)", stripS).group(1))
            return 2**31 - 1 if result > 2**31 - 1 else result
        elif stripS[0] == "+" and stripS[1].isdigit():
            result = int(re.search(r".{1}(\d+)", stripS).group(1))
            return 2**31 - 1 if result > 2**31 - 1 else result
        elif stripS[0] == "-" and stripS[1].isdigit():
            result = - int(re.search(r".{1}(\d+)", stripS).group(1))
            return -2**31 if result < -2**31 else result
        else:
            return 0


# txt = ",,,,,rrttgg.....banana....rrr"
# x = txt.strip(",.grt")
# print(x)  banana  	 Optional. A set of characters to remove as leading/trailing characters
