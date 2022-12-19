import domain.Courseman as cm
import domain.MarkMan as mm
import domain.Sman as sm
import condi as con
import func as fun
c = cm.CourseMan()
m = mm.MarkMan()
s = sm.StudentMan()
while True:
    print("1. Add a new course")
    print("2. Add a new student")
    print("3. Add a new mark")
    print("4. Print all courses")
    print("5. Print all students")
    print("6. Print mark 1 course")
    choice = int(input("Make your choice: "))
    if choice == 1:
        c.appendc()
    if choice == 2:
        s.appends()
    if choice == 3:
        course_choose = input("Enter the course id: ")
        if con.check_course_exist(course_choose,c.getClist()):
            m.appends(course_choose)
        else:
            print("Course not exist")
    if choice == 4:
        c.printlist()
    if choice == 5:
        s.printlist()
    if choice == 6:
        cid = input("Enter the course id: ")
        m.print(cid)
    if choice == 7:
        sid = input("Enter the student id: ")
        if con.check_student_exist(sid,s.getList()):
            m.print_mark_1student(sid)
    if choice == 8:
        sid = input("Enter the student id: ")
        if con.check_student_exist(sid,s.getList()):
            m.calculate_gpa(sid)
    if choice == 9:
        print("Save courses")
        c.save_to_file("courses.txt")
        c.read_file("courses.txt")
    if choice == 10:
        print("Save students")
        s.save_to_file("student.txt")
    if choice == 11:
        print("Save marks ")
        m.save_to_file("mark.txt")
        m.read_file("mark.txt")
    if choice == 12:
        print("Compress data")
        fun.compress_allfile_into_dat()
    if choice == 13:
        print("Decompress data")
        fun.decompress_allfile_into_dat()
        print("Done")
    if choice == 14:
        print("Is the student.dat exist?" ,con.check_file_exist("student.dat"))
    if choice == 0:
        break





    



   