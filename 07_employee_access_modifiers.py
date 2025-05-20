class Employee:
    def __init__(self, name, salary, ssn):
        #public
        self.name = name    
        #protected      
        self._salary = salary  
        #private   
        self.__ssn = ssn         


emp = Employee("Alina", 70000, "123-45-8567")
print(emp.name)           
print(emp._salary)        

print(emp._Employee__ssn)
