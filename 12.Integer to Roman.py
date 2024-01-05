
value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
symbol = ['M', 'CM', 'D', 'CD', 'C', 'XC',
          'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']


num = 3

num_1000 = num // 1000
num_100 = (num % 1000) // 100
num_10 = (num-num_1000*1000-num_100*100) // 10
num_1 = (num-num_1000*1000-num_100*100 - num_10 * 10)


result = ''

if num_1000 >= 0:
    result = num_1000 * symbol[0]

if num_100 == 9:
    result += symbol[1]

if 6 <= num_100 <= 8:
    result += symbol[2]+(num_100-5)*symbol[4]

if num_100 == 5:
    result += symbol[2]

if num_100 == 4:
    result += symbol[3]

if 4 > num_100 >= 0:
    result += symbol[4]*num_100

if num_10 == 9:
    result += symbol[5]

if 6 <= num_10 <= 8:
    result += symbol[6]+(num_10-5)*symbol[8]

if num_10 == 5:
    result += symbol[6]

if num_10 == 4:
    result += symbol[7]

if 4 > num_10 >= 0:
    result += symbol[8] * num_10


if num_1 == 9:
    result += symbol[9]

if 6 <= num_1 <= 8:
    result += symbol[10]+(num_1-5)*symbol[12]

if num_1 == 5:
    result += symbol[10]

if num_1 == 4:
    result += symbol[11]

if 4 > num_1 >= 1:
    result += symbol[12] * num_1


print(num_1000, num_100, num_10, num_1)

print(result)


value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
symbol = ['M', 'CM', 'D', 'CD', 'C', 'XC',
          'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

result = ''

for i in range(len(value)):
    while num >= value[i]:
        num -= value[i]
        result += symbol[i]

return result
