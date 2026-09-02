# try, except, finally  (handle the any type of exception or error in the python)


x=10
y=0

try:
    print(x/y)
except ZeroDivisionError:
    print('you cannot divide a value by zero (it is mathematically wrong)')
finally: # To clean the memory
    print('finally executed')    


