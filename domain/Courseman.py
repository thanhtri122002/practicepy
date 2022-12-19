import  domain.Course as c

class CourseMan:
    def __init__(self) ->None:
        self.__clist = []
    
    def getClist(self):
        return self.__clist
    
    def setClist(self,clist):
        self.__clist = clist
    
    def numberlist(self):
        no = int(input("Enter number of course"))
        return no
    
    def appendc(self):
        number = self.numberlist()
        for i in range(number):
            course = c.Course()
            course.input()
            self.__clist.append(course)
    def printlist(self):
        for i in self.__clist:
            print(f'course:{i.getName()} id: {i.getId()}')

    def save_to_file(self,filename):
        with open(filename,'w') as f:
            for i in self.__clist:#read the object in the course list
                f.write(f'{i.getName()} \t{i.getId()}\n')
            print(type(f))
    
    def read_file(self,filename):
        with open(filename,"r") as f:
            for line in f.readlines():
                print(line)


