class Solution:
    def reverse(x: int) -> int:
        num = 0
        a = abs(x)
        while (a != 0):
            temp = a % 10
            num = num * 10 + temp
            a = int(a/10)

        if x > 0 and num < 2147483647:
            return num
        elif x < 0 and num <= 2147483647:
            return -num
        else:
            return 0


Solution.reverse(-3124235452346)

   if x >= 0:
        y = int(str(x)[::-1])
        return y if y < 2147483648 else 0

    else:
        y = -int(str(x)[:0:-1])  # 排除0 位置，-号
        return y if y > -2147483648 else 0
