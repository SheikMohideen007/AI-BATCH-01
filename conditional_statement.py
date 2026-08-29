#Person -> Adult (>=18), Teenager (>12),Child (<=12),New Born Baby(<3) 

person_age=3

if(person_age>=18):
    print("Person is a Adult")
elif(person_age>12):
    print("person is a Teenager")
elif(person_age<=12 and person_age>=4):
    print("Person is a Child")
else:
    print("New Born baby")    


#TODO: voting system  (18 > vote < not eligible)  
#TODO: switch (practice the 2)


#Exam Grading system
mark=75

if(mark>=90):
    print("GRADE A")
elif mark>=70:
    print("GRADE B")
elif mark>=60:
    print("GRADE C")
elif mark>=50:
    print("PASS")        
else:
    print("FAIL")



