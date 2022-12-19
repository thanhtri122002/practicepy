from numpy import number
import domain.Student as s

class StudentMan:
    def __init__(self)->None:
        self.__slist = []
    
    def getList(self):
        return self.__slist
    
    def setList(self,slist):
        self.__slist = slist
    
    def numberlist(self):
        no = int(input("Enter number of student"))
        return no
    
    def appends(self):
        number = self.numberlist()
        for i in range(number):
            sc = s.Student()
            sc.input()
            self.__slist.append(sc)
    
    def printlist(self):
        for i in self.__slist:
            print(f'name:{i.getName()} \tid: {i.getId()} \tDob:{i.getDob()}')

    def save_to_file(self,filename):
        with open(filename,'w') as f:
            for i in self.__slist:
                f.write(f'{i.getName()} \t{i.getId()} \t{i.getDob()}\n')





