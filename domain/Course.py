class Course:
    def __init__(self):
        self.__id = ""
        self.__name =""
        
    def setName(self,name):
        self.__name = name
    
    def getName(self):
        return self.__name

    def setId(self,id):
        self.__id = id
    
    def getId(self):
        return self.__id

    def input(self):
        self.__id = input("Enter the id of the course: ")
        self.__name = input("Enter the name of the course: ")
    def print(self):
        return f'course:{self.__name}\nid:{self.__id}'
    
    