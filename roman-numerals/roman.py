from collections import OrderedDict

roman_num = OrderedDict()
roman_num[1000] = "M",
roman_num[900] = "CM",
roman_num[500] = "D",
roman_num[400] = "CD",
roman_num[100] = "C",
roman_num[90] = "XC",
roman_num[50] = "L",
roman_num[40] = "XL",
roman_num[10] = "X",
roman_num[9] = "IX",
roman_num[5] = "V",
roman_num[4] = "IV",
roman_num[1] = "I"


def numeral(n):
    res = ""
    for k in roman_num.keys():

        times, remainder = divmod(n, k)
        res += roman_num[k][0]*times
        n = remainder
    return res