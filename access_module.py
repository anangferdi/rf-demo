import example

print(example.add(3, 5))

### Python Exception Handling
"""
Errors that occur at runtime are called exceptions. 
They occur, for example, when a file we try to open does not exist FileNotFoundError, 
dividing a number by zero ZeroDivisionError etc.
"""
# import module sys to get the type of exception
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!",sys.exc_info()[0],"occurred.")
        print("Next entry.")
        print()
print("The reciprocal of",entry,"is",r)