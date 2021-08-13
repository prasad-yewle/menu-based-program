#MODEL WHICH HOLD THE CLASS OF EMPLOYEE which object collection
class Employee:
    def __init__(self,_id = 0,name = None,salary = 0.0):
          self.empId = _id
          self.empName = name
          self.empSalary = salary
    def __repr__(self):
        return f'{self.empId} {self.empName} {self.empSalary}'
     

    