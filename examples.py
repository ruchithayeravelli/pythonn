# 1)Given the total seconds, compute and print equivalent hours, minutes, and seconds using arithmetic operations.
second= 3650
# we want hours so we cant divide with seconds per hour
hours = second // 3600
#we can convert to min to get min
min= (second % 3600)//  60
# to get min we use mod bec get remainder
sec =second % 60
print("hours:",hours ,"min:",min,"sec:",sec)
# 2)Assign the price and quantity of two products. Calculate the total cost including 18% tax. Print a detailed bill?
biscuit = 20
qunt=5
choc= 5
qun=5
pr1=(biscuit*qunt)
pr2 =(choc*qun)
subtotal= pr1 + pr2
print("subtotal :",subtotal)
tax = subtotal* 0.18
# here y total means we added with tax 
total = subtotal +tax
print("Total costt with tax  to  pay :",total)
#3)compute the perimeter and area of a circle given a radius. Use the value of π from the math module.
radius = 7
primiter=2*3.14*radius
radius=3.14*radius*radius
print("primiter:",primiter)
print("radius:",radius)
#  with import math madule
import math
r=float(input("Enter a number:"))
# 4)p formula 2XpiXR
p=(2*math.pi*r)
# area = pi.r square
a=math.pi*r*r
print(p)
print(a)
# Given a temperature in Celsius, convert it to Fahrenheit using the formula and print both values.
#    (F = C × 9/5 + 32)
C=87
F= C*9/5+32
print(F,"F")
# 5) What is a compiled language? What is an interpreted language?
#    Explain pros and cons of each. How hybrid languages bring in advantages of both.
#  PVM and JVM (Super Simple Explanation)
# PVM = Python Virtual Machine
# 👉 It runs Python bytecode.
# 👉 Example: When you run a Python program, PVM executes it and shows output.

# JVM = Java Virtual Machine
# 👉 It runs Java bytecode.
# 👉 Example: When you run a Java program, JVM executes it and shows output.

# ✅ Think Like This
# 🔹 Python Program → compiled to .pyc → PVM runs it
# 🔹 Java Program → compiled to .class → JVM runs it
# 6)Draw the diagram of how a Python program is executed.

#  Source Code (.py / .java)
#           │
#           ▼
#    Compiler → Bytecode (fast)
#           │
#           ▼
# Virtual Machine (PVM / JVM)
#           │
#           ▼
#        Output
#