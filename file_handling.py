# read the sample.txt file
# with open('sample.txt','r') as file:  
#     print(file.read())

# TODO : explore readLine() and readLines()


# w -> it will override the existing content
# with open('sample.txt','w') as file:
#     file.write('Hello from Python')


# a -> append (it will add the content at the end of the existing content)
with open('sample.txt','a') as file:
    file.write(', and SQL')    

# TODO : No file to be there [try append, write, read] -> exception [you needed to handle with try and except]  
