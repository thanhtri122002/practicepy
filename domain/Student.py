
class Student:
    def __init__(self):
        self.__name = ""
        self.__id = ""
        self.__Dob = ""
    
    def setName(self,name):
        self.__name = name
    
    def getName(self):
        return self.__name

    def setId(self,id):
        self.__id = id
    
    def getId(self):
        return self.__id

    def setDob(self,Dob):
        self.__Dob = Dob
    
    def getDob(self):
        return self.__Dob
    def input(self):
        self.__name = input("Enter name: ")
        self.__id = input("Enter id: ")
        self.__Dob = input("Enter dob: ")
    def __str__(self):
         return f'Name: {self.__name} \n id: {self.__id} \n Dob:{self.__Dob}'

