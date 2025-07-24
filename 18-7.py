#Shorthand Operations in Python (with Examples & Possible Errors)
#Shorthnad Operations are Assignment Operator
# =,+=,-=,*=,/=,//=,%=,**=
# 1) =(we are assign  = operator to the variable)
num1 = 15
num1 += 10 
print(num1)
#2) +=(we will reassign the value  of the variable)
num2 =  10
#num2=num2+6 
num2 += 6
print(num2)
#3) -=(we will reassign the value of the variable)
num3= 56
num3 -= 6
print(num3)
#4) *=(we will reassign the value of the variable)
num4 = 20
num4 *= 4
print(num4)
#5) /=(we will reassign the value of the variable)
num5 = 10
num5 /= 3
print(num5)
num =0
num //= 12
print(num)
#6) //=(we will re assign the value of the variable)
num6 = 10
num6 //= 3
print(num6)
#7) **=
num7 = 3
num7 **= 3
print(num7)
print(type(num6))
p="hello"
p  += "hi"
print(p)
hi=[2,4,6]
hi += [5]
print(hi)
#  Errors:
## hii=[2,5,9]
# hii -= [5]
# print(hii)
# TypeError: unsupported operand type(s) for -=: 'list' and 'list'
##num += 23
# print(num)
# NameError: name 'num' is not defined. Did you mean: 'sum'?
##list = [3,4,5,6]
# list -= [6]
#  print(list)
# TypeError: unsupported operand type(s) for -=: 'list' and 'list'
## str = "Hai this ruchitha"
# str += 6
# print(str)
# TypeError: can only concatenate str (not "int") to str
# x = 10
# x **= 10000
# print(x)
# ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
