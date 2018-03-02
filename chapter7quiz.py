Python 3.4.1 (v3.4.1:c0e311e010fc, May 18 2014, 10:38:22) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
f = open("file.txt", "r")
Traceback (most recent call last):
  File "<pyshell#0>", line 2, in <module>
    f = open("file.txt", "r")
FileNotFoundError: [Errno 2] No such file or directory: 'file.txt'
>>> try:
	num = float("10")
	except:
		
SyntaxError: invalid syntax
>>> 
try:
	num = float("10")
	except:
		
SyntaxError: invalid syntax
>>> 
try:

    num = float("10")

except:

    print("Exception!", end=" ")


else:

    print(num, end=" ")




 
 print("End.") 

SyntaxError: unindent does not match any outer indentation level
>>> 
try:
    num = float("10")
except:
    print("Exception!", end=" ")
else:
    print(num, end=" ")
 print("End.")
 
SyntaxError: unindent does not match any outer indentation level
>>> 
try:
    num = float("10")
except:
    print("Exception!", end=" ")
else:
    print(num, end=" ")

 print("End.")
 
SyntaxError: unindent does not match any outer indentation level
>>> 
try:
    print(float("ten"))
except(TypeError):
    print("TypeError")
except(ValueError):
    print("ValueError")

    
ValueError
>>> 
try:
	num = float("ten")
except:
	print("Exception!", end="")

	
Exception!
>>> print("End
      
SyntaxError: EOL while scanning string literal
>>> 
try:
    print(float(None))
except(TypeError):
    print("TypeError")
except(ValueError):
    print("ValueError")

    
TypeError
>>> 
class Critter(object):
    """A virtual pet"""
    def __init__(n="Steve"):
        self.name = n

crit = Critter("Larry")

print(crit.name)
print(crit.name)


          



          
