def input_no_student():
    number = int(input("Enter number of student"))
    return number

def input_no_course():
    number = int(input("Enter number of course"))
    return number

def inputinfo_student():
    #students = {id:{"name":, "Dob": mark:{cid:mark} } }
    students = []
    for i in range(0,input_no_student()):
        id = input("Enter the id of student: ")
        name = input("Enter the name of student: ")
        dob = input("Enter the dob of student: ")
        #a student dictionary 
        student = {"id":id,"name":name, "Dob":dob,"marks":{}}
        students.append(student)
    return students
    
def inputinfo_course():
    courses = []
    for i in range(0,input_no_course()):
        id = input("Enter the id of course: ")
        name = input("Enter the name of course: ")
        course = {"id":id,"name":name}
        courses.append(course)
    return courses

def show_student(students):
    for i in students:
        print(f'ID: {i["id"]} \t Name: {i["name"]} \t Dob: {i["Dob"]}')
def show_course(courses):
    for i in courses:
        print(f'courses:{i["name"]} \t id: {i["id"]}')

def select_course(cid,clist):
    pass
    
            
def input_mark_1course(course,slist):
    for i in slist:
        mark = input(f'Enter the mark of student {i["id"]}: ')
        i["marks"][course] = mark

    
def showmark_course(course,slist):
    for i in slist:
        print(f'Student: {i["id"]} \t Cid:{course} \t Mark:{i["marks"][course]}')

