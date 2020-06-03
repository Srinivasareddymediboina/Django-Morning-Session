class Student:

    def __init__(a,name,rollno):#it is a contructor
        a.name=name
        a.rollno=rollno

    def display(a):
        return {"Name":a.name,'RollNo':a.rollno}
        
        
obj=Student("Srinivas",505)
print(obj.display())
