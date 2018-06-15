"""
Multiplication using improved method by author.
乘法，使用一种自己稍稍改变的方法，蠢蠢的，但更简单。
"""
MultiType = {
    "11": '1' , "21": '2' , "31": '3' , "41": '4' , "51": '5' , "61": '6' , "71": '7' , "81": '8' , "91": '9' ,  # 大九九
    "12": '2' , "22": '4' , "32": '6' , "42": '8' , "52": '10', "62": '12', "72": '14', "82": '16', "92": '18',
    "13": '3' , "23": '6' , "33": '9' , "43": '12', "53": '15', "63": '18', "73": '21', "83": '24', "93": '27',
    "14": '4' , "24": '8' , "34": '12', "44": '16', "54": '20', "64": '24', "74": '28', "84": '32', "94": '36',
    "15": '5' , "25": '10', "35": '15', "45": '20', "55": '25', "65": '30', "75": '35', "85": '40', "95": '45',
    "16": '6' , "26": '12', "36": '18', "46": '24', "56": '30', "66": '36', "76": '42', "86": '48', "96": '54',
    "17": '7' , "27": '14', "37": '21', "47": '28', "57": '35', "67": '42', "77": '49', "87": '56', "97": '63',
    "18": '8' , "28": '16', "38": '24', "48": '32', "58": '40', "68": '48', "78": '56', "88": '64', "98": '72',
    "19": '9' , "29": '18', "39": '27', "49": '36', "59": '45', "69": '54', "79": '63', "89": '72', "99": '81',
};

AddTypeI = [  ##直接加
    "01", "11", "21", "31", "51", "61", "71", "81",  # 一上一
    "02", "12", "22", "52", "62", "72",  # 二上二
    "03", "13", "53", "63",  # 三上三
    "04", "54",  # 四上四
    "05", "15", "25", "35", "45",  # 五上五
    "06", "16", "26", "36",  # 六上六
    "07", "17", "27",  # 七上七
    "08", "18",  # 八上八
    "09"  # 九上九
]
AddTypeII = [  ##满五加
    "41",  # 一下五去四
    "32", "42",  # 二下五去三
    "23", "33", "43",  # 三下五去二
    "14", "24", "34", "44"  # 四下五去一
]
AddTypeIII = [  ##进位加
    "91",  # 一去九进一
    "82", "92",  # 二去八进一
    "73", "83", "93",  # 三去七进一
    "64", "74", "84", "94",  # 四去六进一
    "55", "65", "75", "85", "95",  # 五去五进一
    "46", "96",  # 六去四进一
    "37", "47", "87", "97",  # 七去三进一
    "28", "38", "48", "78", "88", "98",  # 八去二进一
    "19", "29", "39", "49", "69", "79", "89", "99"  # 九去一进一
]
AddTypeIV = [  ##破五进位加
    "56", "66", "76", "86",  # 六上一去五进一
    "57", "67", "77",  # 七上二去五进一
    "58", "68",  # 八上三去五进一
    "59"  # 九上四去五进一
]

abacus = [  # 21档算盘
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 顶珠
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 上珠

    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 下珠
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 底珠
]
Column_abacus = len(abacus[0])


def finger_abacus(number, place, abacus):  # 拨珠子
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


def meter_abacus(number_list, abacus):  # 算盘面
    number_len = len(number_list)
    for i in range(number_len, 0, -1):
        finger_abacus(int(number_list[-i]), -i, abacus)
    return abacus


def number_Split(number):  # 分为整数部与小数部
    if "." in list(str(number)):
        number_list = str(number).split('.')
        number_Integer = number_list[0]
        number_Decimal = number_list[1]
    else:
        number_Integer = str(number)
        number_Decimal = ""
    return number_Integer, number_Decimal


def number_Align_Integer(number_1, number_2):  # 整数对齐
    number_1_list = list(str(number_1))
    number_2_list = list(str(number_2))
    number_1_len = len(number_1_list)
    number_2_len = len(number_2_list)
    length = max(number_1_len, number_2_len)
    number_1_temp = ["0"] * (length - number_1_len)
    number_2_temp = ["0"] * (length - number_2_len)
    number_1_temp.extend(number_1_list)
    number_2_temp.extend(number_2_list)
    return number_1_temp, number_2_temp


def number_Align_Decimal(number_1, number_2, Num_Decimal):  # 小数对齐
    number_1_list = list(str(number_1))
    number_2_list = list(str(number_2))
    number_1_len = len(number_1_list)
    number_2_len = len(number_2_list)
    length = Num_Decimal
    number_1_temp = ["0"] * (length - number_1_len)
    number_2_temp = ["0"] * (length - number_2_len)
    number_1_list.extend(number_1_temp)
    number_2_list.extend(number_2_temp)
    return number_1_list, number_2_list


def Addition(number_1, number_2, abacus):  # 加法主函数
    number_1_Integer, number_1_Decimal = number_Split(number_1)
    number_2_Integer, number_2_Decimal = number_Split(number_2)
    Aygend_align_Integer, Addend_align_Integer = number_Align_Integer(number_1_Integer,
                                                                      number_2_Integer)  # 对齐 ['7', '2', '7'] ['1', '1', '9']
    Aygend_align_Decimal, Addend_align_Decimal = number_Align_Decimal(number_1_Decimal, number_2_Decimal,
                                                                      Num_Decimal)  # 对齐 ['0', '0', '0'] ['0', '0', '0']
    Aygend_align = Aygend_align_Integer + Aygend_align_Decimal
    Addend_align = Addend_align_Integer + Addend_align_Decimal
    Aygend_abacus = meter_abacus(Aygend_align, abacus)  # 被加数拨数
    len_temp = len(Aygend_align)
    for i in range(len_temp):
        a = Aygend_align[i]
        b = Addend_align[i]
        place = -(len_temp - i)
        type = a + b
        if b == '0':
            pass
        elif type in AddTypeI:
            if b == "1":
                abacus[2][place] += 1
            elif b == "2":
                abacus[2][place] += 2
            elif b == "3":
                abacus[2][place] += 3
            elif b == "4":
                abacus[2][place] += 3
            elif b == "5":
                abacus[1][place] += 1
            elif b == "6":
                abacus[1][place] += 1
                abacus[2][place] += 1
            elif b == "7":
                abacus[1][place] += 1
                abacus[2][place] += 2
            elif b == "8":
                abacus[1][place] += 1
                abacus[2][place] += 3
            elif b == "9":
                abacus[1][place] += 1
                abacus[2][place] += 4
        elif type in AddTypeII:
            abacus[1][place] += 1
            if b == "1":
                abacus[2][place] -= 4
            elif b == "2":
                abacus[2][place] -= 3
            elif b == "3":
                abacus[2][place] -= 2
            elif b == "4":
                abacus[2][place] -= 1
        elif type in AddTypeIII:
            for j in range(9999):
                if abacus[2][place - 1 - j] != 4:  # 进位检查
                    abacus[2][place - 1 - j] += 1
                    break
                elif abacus[2][place - 1 - j] == 4 and abacus[1][place - 1 - j] == 0:
                    abacus[2][place - 1 - j] = 0
                    abacus[1][place - 1 - j] = 1
                elif abacus[2][place - 1 - j] == 4 and abacus[1][place - 1 - j] == 1:
                    abacus[2][place - 1 - j] = 0
                    abacus[1][place - 1 - j] = 0
            if b == "1":
                abacus[1][place] -= 1
                abacus[2][place] -= 4
            elif b == "2":
                abacus[1][place] -= 1
                abacus[2][place] -= 3
            elif b == "3":
                abacus[1][place] -= 1
                abacus[2][place] -= 2
            elif b == "4":
                abacus[1][place] -= 1
                abacus[2][place] -= 1
            elif b == "5":
                abacus[1][place] -= 1
            elif b == "6":
                abacus[2][place] -= 4
            elif b == "7":
                abacus[2][place] -= 3
            elif b == "8":
                abacus[2][place] -= 2
            elif b == "9":
                abacus[2][place] -= 1
        elif type in AddTypeIV:
            abacus[1][place] -= 1
            for j in range(9999):  # 进位检测
                if abacus[2][place - 1 - j] != 4:
                    abacus[2][place - 1 - j] += 1
                    break
                elif abacus[2][place - 1 - j] == 4 and abacus[1][place - 1 - j] == 0:
                    abacus[2][place - 1 - j] = 0
                    abacus[1][place - 1 - j] = 1
                elif abacus[2][place - 1 - j] == 4 and abacus[1][place - 1 - j] == 1:
                    abacus[2][place - 1 - j] = 0
                    abacus[1][place - 1 - j] = 0
            if b == "6":
                abacus[2][place] += 1
            elif b == "7":
                abacus[2][place] += 2
            elif b == "8":
                abacus[2][place] += 3
            elif b == "9":
                abacus[2][place] += 4
    return Aygend_abacus


def Multiplication(number_1, number_2, abacus):  # 乘法主函数
    number_1_Integer, number_1_Decimal = number_Split(number_1)
    number_2_Integer, number_2_Decimal = number_Split(number_2)
    multiplicand_align_Integer, multiplier_align_Integer = number_Align_Integer(number_1_Integer,number_2_Integer)  # 对齐 ['7', '2', '7'] ['1', '1', '9']
    multiplicand_align_Decimal, multiplier_align_Decimal = number_Align_Decimal(number_1_Decimal, number_2_Decimal,Num_Decimal)  # 对齐 ['0', '0', '0'] ['0', '0', '0']
    multiplicand_align = multiplicand_align_Integer + multiplicand_align_Decimal
    multiplier_align = multiplier_align_Integer + multiplier_align_Decimal
    len_temp = len(multiplicand_align)
    product = '0'
    product_void = abacus
    product_abacus = abacus
    for i in range(len_temp):
        for j in range(len_temp):
            a = multiplicand_align[-(j + 1)]
            b = multiplier_align[-(i + 1)]
            if a == '0' or b == '0':
                product_temp = '0'
                pass
            else:
                type = a + b
                tail = ''.join(['0'] * (i+j))
                product_temp = MultiType[type] + tail
            product = ''.join(abacusToString(Addition(product, product_temp, product_void)).split('.'))            
            product_abacus = meter_abacus(list(product), abacus)                      #十分多余的逆运算，但有仪式感
    return product_abacus


def abacusToNumber(abacus):  # 算盘读数为数字
    number_abacus = 0
    for i in range(Column_abacus):
        number_abacus = number_abacus + abacus[1][i] * 5 * pow(10, Column_abacus - 1 - i - Num_Decimal) + abacus[2][
            i] * 1 * pow(10, Column_abacus - 1 - i - Num_Decimal)
    return number_abacus


def abacusToString(abacus):  # 算盘读数为字符串
    string_abacus = ""
    for i in range(Column_abacus - Num_Decimal):
        number_temp = abacus[1][i] * 5 + abacus[2][i] * 1
        string_abacus = string_abacus + str(number_temp)
    if Num_Decimal > 0:
        string_abacus = string_abacus + "."
    for i in range(Column_abacus - Num_Decimal, Column_abacus):
        number_temp = abacus[1][i] * 5 + abacus[2][i] * 1
        string_abacus = string_abacus + str(number_temp)
    string_list = list(string_abacus)
    for i in list(string_abacus):
        if i != "0":
            break
        else:
            string_list.pop(0)
    string = ''.join(string_list)
    return string


product_abacus = abacus  # 初始化算盘

multiplicand = 727.727  # 定义被乘数，“实数”     "727"
multiplier = 119.119  # 定义乘数，“法数”       "119"

# Num_Decimal = 3                                                                         #定义小数位数   3
Num_Decimal = len(number_Split(multiplicand)[1]) + len(number_Split(multiplier)[1])  # 小数根据给定数字确定

result = abacusToString(Multiplication(multiplicand, multiplier, product_abacus))  # 计算结果
print(result)  # 输出结果