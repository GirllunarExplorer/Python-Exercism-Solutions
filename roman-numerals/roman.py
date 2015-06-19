
roman_num = {1000: "M",
             500: "D",
             100: "C",
             50: "L",
             10: "X",
             5: "V",
             3: "III",
             2: "II",
             1: "I"}
def checker(n):
    string_n = str(n)
    f_n = int(string_n[0])
    new_n, first_num, sec_num = [0,0,0]
    if f_n == 4:
        new_n = int("4"+ ("0"* (len(string_n)-1))) #sets the integer to 4, 40, 400, etc
        first_num = int("1"+ ("0"* (len(string_n)-1)))  #sets the first character to be retrieved to 1, 10, 100, 1000, etc.
        sec_num = int("5"+ ("0"* (len(string_n)-1)))  #sets the second character to be retrieved to 5, 50, 500, 5000, etc.
        return new_n, (roman_num[first_num] + roman_num[sec_num])

    elif f_n in range(6, 9):
        diff = f_n-5
        new_n = int(str(f_n) +("0"* (len(string_n)-1)))
        first_num = int("5"+ ("0"* (len(string_n)-1))) # sets the first character to 5, 50, 500
        sec_num = int(str(1)+"0"*(len(string_n)-1)) # sets the second char 1s, 10s, 100s
        sec_str = ""
        for in range(diff):
            # appends the correct '1' digit however many times compared to the difference between n and 5
            sec_str += roman_num[sec_num]
        return new_n, (roman_num[first_num] + sec_str)

    elif f_n == 9:
        new_n = int("9"+ ("0"* (len(string_n)-1)))
        first_num = int("1"+ ("0"* (len(string_n)-1))) # finds the 10 ** len(n)-1
        sec_num = int("1"+ ("0"* len(string_n))) # finds 10 ** len(n).
                                                # For example IX is 10 -1 so the first_num
                                                # finds "1" and the sec_num finds "10"
        return new_n, (roman_num[first_num]+ roman_num[sec_num])

    else: pass


def numeral(n):
    result = ""
    if len(str(n)) == 4:
        while n >= 1000:
            result += "M"
            n -= 1000
    while n > 0:
        if checker(n): #checks for 4,6,7,8
            result += checker(n)[1]
            n -= checker(n)[0]
        elif str(n)[0] == "5":  # checks for 5, 50, 500
            n_5 = int("5"+ ("0"* (len(str(n))-1)))
            result += roman_num[n_5]
            n -= n_5

        else:
            if len(str(n)) != 1:
                tens = int("1"+ ("0"* (len(str(n))-1)))
                result += roman_num[tens]
                n-= tens
            else:
                result += roman_num[n]
                n -= n
    return result