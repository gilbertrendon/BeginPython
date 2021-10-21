class EmpNameDescriptor:
    def __get__(self, obj, owner):
        return self.__empname
    def __set__(self, obj, value):
        if not isinstance(value, str):
            raise TypeError("'empname' must be a string.")
        self.__empname = value

class EmpIdDescriptor:
    def __get__(self, obj, owner):
        return self.__empid
    def __set__(self, obj, value):
        if hasattr(obj, 'empid'):
            raise ValueError("'empid' is read only attribute")
        if not isinstance(value, int):
            raise TypeError("'empid' must be an integer.")
        self.__empid = value
        
class Employee:
    # def __init__(self, emp_id, emp_name):
    #     self.empid = emp_id
    #     self.empname = emp_name
    # @property
    # def empid(self):
    #     return self.__empid
    # @empid.setter
    # def empid(self, value):
    #     if not isinstance(value, int):
    #         raise TypeError("'empid' must be an integer.")
    #     self.__empid = value
    # @property
    #     def empname(self):
    #         return self.__empname
    #     @empname.setter
    #     def empname(self, value):
    #         if not isinstance(value, str):
    #             raise TypeError("'empname' must be a string.")
    #         self.__empname = value
    #     @empname.deleter
    #     def empname(self):
    #         del self.__empname



    def __init__(self, emp_id, emp_name):
        self.empid = emp_id
        self.empname = emp_name
    def getempid(self):
        return self.__empid
    def setempid(self, value):
       if not isinstance(value, int):
            raise TypeError("'empid' must be an integer.")
            self.__empid = value
        #empid = property(getEmpID, setEmpID)
    
    def getEmpName(self):

        return self.__empname



    def setEmpName(self, value):

        if not isinstance(value, str):

            raise TypeError("empname' must be a string.")

        self.__empname = value



    def delempname(self):
        print('qwerqwerwqrwqrwqer')

        del self.empname



    empname = property(getEmpName, setEmpName, delempname)



if __name__ == "__main__":
    print('asdfasdffsd')
    e1 = Employee(123456, 'John')
    print(e1.empid, '-', e1.empname)    # -> '123456 - John'
    Employee.delempname(e1)    # Deletes 'empname'
    print(e1.empname) #Raises 'AttributeError'
    # objeto = EmpNameDescriptor();
    # objeto.__empname = 'cuerco'
    # e1 = Employee(123456, 'John')
    # print(e1.empid, '-', e1.empname)  
    # e1.empname = 'Williams'
    # print(e1.empid, '-', e1.empname)
