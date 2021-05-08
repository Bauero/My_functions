#program converts the number into a number system of a given base
def konwersja_liczb (number,sys_base):
    
    #next number by which we can divide our number
    max_divider = sys_base

    #all dividers smaller than our number being next powers of our sys_base (for 2 those are 1,2,4,8,16,32 ...)
    dividers = [1]

    result=''

    #program find all powers of base system smaller than our number
    while max_divider <= number:
        dividers.append(max_divider)
        max_divider*=sys_base

    #program finds how many multilples of our dividers are in our number
    for i in reversed(dividers):
        result += str(number//i)
        number-=(i*(number//i))

    return result
