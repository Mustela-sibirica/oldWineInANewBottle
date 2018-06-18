"""
今有物，不知其数。三、三数之，剩二；五、五数之，剩三；七、七数之，剩二。问物几何？
答曰：二十三。
术曰：“三、三数之，剩二”，置一百四十；“五、五数之，剩三”，置六十三；“七、七数之，剩二”，置三十。并之，得二百三十三。以二百一十减之，即得。
"""

number_1 = 0
number_2 = 0
number_3 = 0
i = 0
while True:
    number_1 = i
    if i % 3 == 2 and  i % 5 == 0 and i % 7 == 0:
        break
    i += 1
j = 0
while True:
    number_2 = j
    if j % 5 == 3 and  j % 3 == 0 and j % 7 == 0:
        break
    j += 1
k = 0
while True:
    number_3 = k
    if k % 7 == 2 and  k % 3 == 0 and k % 5 == 0:
        break
    k += 1
number = number_1 + number_2 + number_3
tail = 3*5*7
while True:
    number -= tail
    if number - tail < 0:
        break
result = "the result is " + str(int(number)) + " + k×" + str(int(tail)) + ", k∈N."
print(result)
