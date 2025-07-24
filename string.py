str1 = "Jayalaxmi"
# First char of the given string
print("first char:",str1[0])
#Second char of the given string
print("Second char:",str1[-1])
#char in between 2 t0 5
print(str1[2:6])
# Concatenate two strings and print the result?
n = 'Hai this'
m = ' is Ruchitha'
print(n+m)
# Define list. What are the difference between List and Tuple? example
list_1 = [3,'ahi' ,5.8 ,4,2,3,[5,7,5]]
# update
list_1[0] ="nani"
# printing list in list last index
print(list_1[6][-1])
#print list
print(list_1)
tuple_1=( 4, 5 , "hai", 7)
print(tuple_1)
#5.	Write a programme to print a list in reverse order?
list_3=[9,7,3,5,6]
print(list_3[::-1])
#6)Create a tuple of 4 elements. Print the first and last element?
tuple_2  =  ( 4, 5, 8, 9)
print(tuple_2[0])
print(tuple_2[-1])
# creating dictionary
dict_1 = {
    'Ruchitha':48,
    'Vijay': 45,
    'jayalaxmi': 39
}
print(dict_1)
# Access the marks of one student using their name.
print(dict_1['jayalaxmi'])
# Update the marks of an existing student
dict_1['Ruchitha']=57
print(dict_1)
#  Print all multiples of 17 using range. Numbers should start from -34 and end below 400.
print(list(range(-34,400,17)))
# Source Code (.py / .java)
#           │
#           ▼
#    Compiler → Bytecode (fast)
#           │
#           ▼
# Virtual Machine (PVM / JVM)
#           │
#           ▼
#        Output
#MULTI LINE COMMENT      
'''
This is a multi-line comment example.
Technically, it's a multi-line string,
but since it is not assigned to a variable,
Python ignores it.
'''

print("Hello, Python!")
