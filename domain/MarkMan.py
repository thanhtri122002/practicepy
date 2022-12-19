import domain.Mark as m
import domain.Courseman as c
import domain.Sman as s
import numpy as np
class MarkMan:
    def __init__(self)-> None:
        self.__mlist = []
    
    def getList(self):
        return self.__mlist
    
    def setList(self,mlist):
        self.__mlist = mlist
    
    def appends(self,course):
            sid = input("Enter the student id: ")
            mark = int(input("Enter the mark of student: "))
            MarkForStudent = m.Mark(sid,mark,course)
            self.__mlist.append(MarkForStudent)

    def print(self,course):
        for i in range(0,len(self.__mlist)):
            if self.__mlist[i].getCid() == course:
                print(f'Student: {self.__mlist[i].getSid()} \t Cid:{self.__mlist[i].getCid()} \t Mark:{self.__mlist[i].getMark()}')
    
    def print_mark_1student(self,sid):
        for i in self.__mlist:
            if i.getSid() == sid:
                print(f'Student: {i.getSid()} \t Cid:{i.getCid()} \t Mark:{i.getMark()}')

    def save_to_file(self,filename):
        with open(filename,'w') as f:
            for i in self.__mlist:
                f.write(f'{i.getSid()} \t{i.getMark()} \t{i.getCid()}\n')

    def read_file(self,filename):
        with open(filename,"r") as f:
            f.readlines
    




