

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        res = ''
        for r in range(numRows):
            increment = 2*(numRows-1)

            for i in range(r, len(s), increment):
                # 利用increment 与 row的关系
                res += s[i]
                # 利用i+increment 与 row的关系。下一个i+increment 返回2*r
                if (r > 0 and r < numRows-1 and i+increment - 2*r < len(s)):
                    res += s[i+increment - 2*r]

        return res


# use up (true and false)
        if numRows == 1:
            return s
        row_map = {row: '' for row in range(1, numRows+1)}

        row = 1
        up = True

        for letter in s:
            # numrow = 5 执行5次 转到else
            row_map[row] += letter
            if (row == 1) or ((row < numRows) and up):    # 1 row +1  2 row +1 3 row +1 4 row +1
                row += 1
                up = True

            else:
                row -= 1
                up = False
        coverted = ''
        for row in range(1, numRows+1):
            coverted += row_map[row]
        return coverted
