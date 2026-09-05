import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd

# months=['JAN','FEB','MAR','APR']
# sales=[100,150,130,200]

# # Line Chart

# plt.plot(months,sales)

# plt.xlabel("Month")
# plt.ylabel("Sales")

# plt.title("Monthly Sales")

# plt.show()

# BAR chart
# departments=['IT','HR',"FINANCE"]
# employees=[50,30,20]

# plt.bar(departments,employees)
# plt.xlabel('Department')
# plt.ylabel('Employee')

# plt.title('Employees by Department')

# plt.show()


#Scatter plot
# experience=[1,2,3,4,5]
# salary=[30000,50000,70000,80000,90000]

# plt.scatter(experience,salary)

# plt.xlabel('Experience')
# plt.ylabel('Salary')

# plt.title('Experience vs salary')

# plt.show()


data={
    'Name':['John','Cena','Brock',"Lesnar",'Tom'],
    'Department':[
        "IT","HR","IT","Finance","HR"
    ],
    "Experience":[2,3,4,5,6],
    "Salary":[40000,50000,55000,60000,70000],
    "Gender":[
        "Male","Female","Male","Female","Male"
    ]
}


df = pd.DataFrame(data)

# print(df)

# how many employee are in each department
# sb.countplot(data=df,x="Department")

# plt.title("Employees by Department")

# plt.show()


# sb.barplot(data=df,x="Department",y="Salary")

# plt.title("Average Salary by department")
# plt.show()


#TODO : histogram(), boxplot()

# TODO : try to visualize the Titanic Dataset 