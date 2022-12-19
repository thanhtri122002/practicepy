

import os

def check_course_exist(cid,clist):
    for i in clist:
        if i.getId() == cid:
            
            return True
    return False

def check_student_exist(sid,slist):
    for i in slist:
        if i.getId() == sid:
            return True
    return False

def check_file_exist(filename):
    if os.path.exist(os.getcwd() + "\\" + filename):
        return True
    else:
        return False

def check_duplicate(element, list):
    for i in list:
        if i != element:
            return True
    return False




