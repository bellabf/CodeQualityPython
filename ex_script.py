import math
import os

def Add(a,b):
  result = a+b
  return result

def divideNumbers(a , b ):
    if(b != 0 ):
       return a /b 
    else:
       print("Error: division by zero!")
    return None

def factorial(n):
    f = 1
    for i in range(1, n + 1 ):
       f=f*i
    return f
  
def printResult( x):
  if x is not None:
      print( "The result is: " + str( x ) )
val1=val1
val1 = 10
VAL2 = 0
sum = Add(val1, VAL2)
division = divideNumbers(10, 0)
fact = factorial( 5 )
printResult( sum )
printResult(fact)