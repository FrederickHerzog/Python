from _typeshed import ReadableBuffer
import re                                                                                                                                                                                                                                           


def AreDatesValid(dates):
    #YYYY/MM/DD
    regex = "^\d{4}/(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])$"
    d = []
    for date in dates:
        r = re.match(regex, date)
        if r:
            d.append(date)
        else: 
            print()
            print(date + "  is not a valid date.,,,\n")
    return d

def isEmailValid(addr):
    regex = ''
    r = re.match(regex, addr)
    if r:
        return(addr)
        print(addr)
    else: print("Not a valid Email...")

def time(t):
    regex = ''
    r = re.match(regex, t)
    if r: return t
    else: print("Not a valid time...")

def main():
    dates_list = ["2020/10/05", "2021-09-21", "1999/03/03", "1987/12/12", "1885/02/01", '95-02-10', "20210510"]
    valid_dates = AreDatesValid(dates_list)
    print("******************************")
    print()
    print("These are valid:")
    print("----------------")
    for i, date in enumerate(valid_dates): print(i+1, date)
    print()

main()