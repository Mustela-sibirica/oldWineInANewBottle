"""
Subtraction using spell.
口诀减
"""
MinusTypeI = [                                        ##直接减
     "11","21","31","41",     "61","71","81","91",  #一去一
          "22","32","42",           "72","82","92"  #二去二
               "33","43",               "83","93",  #三去三
                    "44",                    "94",  #四去四
                         "55","65","75","85","95",  #五去五
                              "66","76","86","96",  #六去六
                                   "77","87","97",  #七去七
                                        "88","98",  #八去八
                                             "99"   #九去九
]
MinusTypeII = [                                       ##破五加
                         "51",                      #一上四去五
                         "52","62",                 #二上三去五
                         "53","63","73",            #三上二去五
                         "54","64","74","84"        #四上一去五
]
MinusTypeIII = [                                      ##退十减
 "01",                                              #一退十还九
 "02","12",                                         #二退十还八
 "03","12","23",                                    #三退十还七
 "04","14","24","34",                               #四退十还六
 "05","15","25","35","45",                          #五退十还五
 "06",                    "56",                     #六退十还四
 "07","17",               "57","67",                #七退十还三
 "08","18","28",          "58","68","78",           #八退十还二
 "09","19","29","39",     "59","69","79","89"       #九退十还一


]
MinusTypeIV = [                                       ##退十补五减
      "16","26","36","4",                           #六退十还五去一
           "27","37","47",                          #七退十还五去二
                "38","48",                          #八退十还五去三
                     "49"                           #九退十还五去四
]

abacus = [                                          #21档算盘
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],        #顶珠
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],        #上珠

[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],        #下珠
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]         #底珠
]
Column_abacus = len(abacus[0])

def finger_abacus(number,place,abacus):             #拨珠子
    if number == 0:
        pass
    elif number == 1:
        abacus[2][place] = 1
    elif number == 2:
        abacus[2][place] = 2
    elif number == 3:
        abacus[2][place] = 3
    elif number == 4:
        abacus[2][place] = 4
    elif number == 5:
        abacus[1][place] = 1
    elif number == 6:
        abacus[1][place] = 1
        abacus[2][place] = 1
    elif number == 7:
        abacus[1][place] = 1
        abacus[2][place] = 2
    elif number == 8:
        abacus[1][place] = 1
        abacus[2][place] = 3
    elif number == 9:
        abacus[1][place] = 1
        abacus[2][place] = 4

def meter_abacus(number_list,abacus):               #算盘面
    number_len = len(number_list)
    for i in range(number_len,0,-1):
        finger_abacus(int(number_list[-i]),-i,abacus)
    return abacus

def number_Split(number):                           #分为整数部与小数部
    if "." in list(str(number)):
        number_list = str(number).split('.')
        number_Integer = number_list[0]
        number_Decimal = number_list[1]
    else:
        number_Integer = str(number)
        number_Decimal = ""
    return number_Integer,number_Decimal

def number_Align_Integer(number_1,number_2):        #整数对齐
    number_1_list = list(str(number_1))
    number_2_list = list(str(number_2))
    number_1_len = len(number_1_list)
    number_2_len = len(number_2_list)
    length = max(number_1_len,number_2_len)
    number_1_temp = ["0"] * (length-number_1_len)
    number_2_temp = ["0"] * (length-number_2_len)
    number_1_temp.extend(number_1_list)
    number_2_temp.extend(number_2_list)
    return number_1_temp,number_2_temp

def number_Align_Decimal(number_1,number_2,Num_Decimal):    #小数对齐
    number_1_list = list(str(number_1))
    number_2_list = list(str(number_2))
    number_1_len = len(number_1_list)
    number_2_len = len(number_2_list)
    length = Num_Decimal
    number_1_temp = ["0"] * (length-number_1_len)
    number_2_temp = ["0"] * (length-number_2_len)
    number_1_list.extend(number_1_temp)
    number_2_list.extend(number_2_temp)
    return number_1_list,number_2_list

def Subtraction(number_1,number_2,abacus):                     #主函数
    number_1_Integer,number_1_Decimal = number_Split(number_1)
    number_2_Integer,number_2_Decimal = number_Split(number_2)
    minuend_align_Integer,subtrahend_align_Integer = number_Align_Integer(number_1_Integer,number_2_Integer)                 #对齐 ['7', '2', '7'] ['1', '1', '9']
    minuend_align_Decimal,subtrahend_align_Decimal = number_Align_Decimal(number_1_Decimal,number_2_Decimal,Num_Decimal)     #对齐 ['0', '0', '0'] ['0', '0', '0']
    minuend_align = minuend_align_Integer + minuend_align_Decimal
    subtrahend_align = subtrahend_align_Integer + subtrahend_align_Decimal
    minuend_abacus = meter_abacus(minuend_align,abacus)                                               #被减数拨数
    len_temp = len(minuend_align)
    for i in range(len_temp):
        a = minuend_align[i]
        b = subtrahend_align[i]
        place = -(len_temp-i)
        type = a + b
        if b == 0:
            pass
        elif type in MinusTypeI:
            if b == "1":
                abacus[2][place] -= 1
            elif b == "2":
                abacus[2][place] -= 2
            elif b == "3":
                abacus[2][place] -= 3
            elif b == "4":
                abacus[2][place] -= 3
            elif b == "5":
                abacus[1][place] -= 1
            elif b == "6":
                abacus[1][place] -= 1
                abacus[2][place] -= 1
            elif b == "7":
                abacus[1][place] -= 1
                abacus[2][place] -= 2
            elif b == "8":
                abacus[1][place] -= 1
                abacus[2][place] -= 3
            elif b == "9":
                abacus[1][place] -= 1
                abacus[2][place] -= 4
        elif type in MinusTypeII:
            abacus[1][place] -= 1
            if b == "1":
                abacus[2][place] += 4
            elif b == "2":
                abacus[2][place] += 3
            elif b == "3":
                abacus[2][place] += 2
            elif b == "4":
                abacus[2][place] += 1
        elif type in MinusTypeIII:
            for j in range(9999):
                if abacus[2][place-1-j] != 0:                                       #进位检查
                    abacus[2][place-1-j] -= 1
                    break
                elif abacus[2][place-1-j] == 0 and abacus[1][place-1-j] == 0:
                    abacus[2][place-1-j] = 1
                    abacus[1][place-1-j] = 1
                elif abacus[2][place-1-j] == 0 and abacus[1][place-1-j] == 1:
                    abacus[2][place-1-j] = 4
                    abacus[1][place-1-j] = 0
            if b == "1":
                abacus[1][place] += 1
                abacus[2][place] += 4
            elif b == "2":
                abacus[1][place] += 1
                abacus[2][place] += 3
            elif b == "3":
                abacus[1][place] += 1
                abacus[2][place] += 2
            elif b == "4":
                abacus[1][place] += 1
                abacus[2][place] += 1
            elif b == "5":
                abacus[1][place] += 1
            elif b == "6":
                abacus[2][place] += 4
            elif b == "7":
                abacus[2][place] += 3
            elif b == "8":
                abacus[2][place] += 2
            elif b == "9":
                abacus[2][place] += 1
        elif type in MinusTypeIV:
            abacus[1][place] = 1
            for j in range(9999):
                if abacus[2][place-1-j] != 0:                                       #进位检查
                    abacus[2][place-1-j] -= 1
                    break
                elif abacus[2][place-1-j] == 0 and abacus[1][place-1-j] == 0:
                    abacus[2][place-1-j] = 1
                    abacus[1][place-1-j] = 1
                elif abacus[2][place-1-j] == 0 and abacus[1][place-1-j] == 1:
                    abacus[2][place-1-j] = 4
                    abacus[1][place-1-j] = 0
            if b == "6":
                abacus[2][place] -= 1
            elif b == "7":
                abacus[2][place] -= 2
            elif b == "8":
                abacus[2][place] -= 3
            elif b == "9":
                abacus[2][place] -= 4
    return minuend_abacus

def abacusToNumber(abacus):                                                            #算盘读数为数字
    number_abacus = 0
    for i in range(Column_abacus):
        number_abacus = number_abacus + abacus[1][i]*5*pow(10,Column_abacus-1-i-Num_Decimal) + abacus[2][i]*1*pow(10,Column_abacus-1-i-Num_Decimal)
    return number_abacus

def abacusToString(abacus):                                                            #算盘读数为字符串
    string_abacus = ""
    for i in range(Column_abacus-Num_Decimal):
        number_temp = abacus[1][i]*5 + abacus[2][i]*1
        string_abacus = string_abacus + str(number_temp)
    if Num_Decimal > 0:
        string_abacus = string_abacus + "."
    for i in range(Column_abacus-Num_Decimal,Column_abacus):
        number_temp = abacus[1][i]*5 + abacus[2][i]*1
        string_abacus = string_abacus + str(number_temp)
    string_list = list(string_abacus)
    for i in list(string_abacus):
        if i != "0":
            break
        else:
            string_list.pop(0)
    string = ''.join(string_list)
    return string

minuend_abacus = abacus                                                             #初始化算盘

minuend = 727                                                                       #定义被减数     "727"
subtrahend = 119                                                                    #定义减数       "119"

#Num_Decimal = 3                                                                    #定义小数位数   3
Num_Decimal = max(len(number_Split(minuend)[1]),len(number_Split(subtrahend)[1]))   #小数根据给定数字确定

result = abacusToString(Subtraction(minuend,subtrahend,minuend_abacus))             #计算结果
print(result)                                                                       #输出结果