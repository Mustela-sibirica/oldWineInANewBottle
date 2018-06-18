"""
鸡兔同笼
今有雉兔同笼，上有三十五头，下九十四足。问雉、兔各几何？
打开字典
答曰：雉二十三。兔一十二。
术曰：上置三十五头，下置九十四足。半其足，得四十七。以少减多，再命之，上三除下三，上五除下五。下有一除上一，下有二除上二，即得。
又术曰：上置头，下置足。半其足，以头除足，以足除头，即得。
"""

def cage(head,foot):
    head = 35                    #35
    foot = 94                    #94
    foot_half = foot/2           #94÷2=47
    rabbit = foot_half - head    #47-35=12
    chicken = head - rabbit      #35-12=23
    return chicken,rabbit
head = 35                    #35
foot = 94                    #94
chicken,rabbit = cage(head,foot)
result = 'There are ' + str(int(chicken)) + ' chickens and ' + str(int(rabbit)) + ' rabbits.'
print(result)