#classes help tocreate a datatype of a real world object
#a class gives a general discription of an object
#an object is an instance of a class or a member of a class

class Employee:
    def __init__(self, name, age, emp_number, contact, is_a_manager):
        self.name=name
        self.age=age
        self.emp_number=emp_number
        self.contact=contact
        self.is_a_manager=is_a_manager
        
employee1=Employee("Tom", 35, "345", 757291160, True)
print(employee1.name)


