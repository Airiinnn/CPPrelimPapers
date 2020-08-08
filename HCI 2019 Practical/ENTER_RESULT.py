class Student:
    
    def __init__(self, StudID, Name, StudType, Result=None):
        self.StudID = StudID
        self.Name = Name
        self.StudType = StudType
        self.NoOfSub = '0'
        self.SkillArea = "Diploma"
        self.Result = Result
        

        
class Diploma(Student):
    
    def __init__(self, StudID, Name, StudType, NoOfSub, Result=None):
        super(Diploma, self).__init__(StudID, Name, StudType, Result)
        self.NoOfSub = NoOfSub
        

        
class SkillsCert(Student):
    
    def __init__(self, StudID, Name, StudType, SkillArea, Result=None):
        super(SkillsCert, self).__init__(StudID, Name, StudType, Result)
        self.SkillArea = SkillArea

        

def read_file(filename):
    data = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            temp = line.strip().split("|")
            
            if temp[2] == 'D':
                data.append(Diploma(temp[0], temp[1], temp[2], temp[4], temp[5]))

            else:
                data.append(SkillsCert(temp[0], temp[1], temp[2], temp[3], temp[5]))

    return data



def write_file(filename, data):
    with open(filename, 'w') as file:
        for line in data:
            file.write(f"{line.StudID}|{line.Name}|{line.StudType}|{line.SkillArea}|{line.NoOfSub}|{line.Result}\n")



def validate_studid(studid):
    if not studid.isdigit(): # data type check
        return False

    elif len(studid) != 6: # length check
        return False

    return True



def validate_result(result, studtype):
    if not result.isalpha(): # data type check
        return False

    elif len(result) != 1: # length check
        return False

    else: # range check
        if studtype == 'D': # diploma
            grades = ['A', 'B', 'C', 'D', 'E', 'F']

        else: # skills certificate
            grades = ['D', 'M', 'P', 'F']

        if result not in grades:
            return False

        return True



def enter_result():
    run = 'Y'

    while run.upper() == 'Y':
        studid = input("StudID: ")

        if validate_studid(studid):
            students = read_file("STUDENT.txt")
            found = False
            
            for student in students:
                if student.StudID == studid:
                    found = True
                    
                    print("{0:6s} {1:12s} {2:8s} {3:9s} {4:7s} {5:6s}".format("StudID", "Name", "StudType", "SkillArea", "NoOfSub", "Result"))
                    print("{0:6s} {1:12s} {2:8s} {3:9s} {4:7s} {5:6s}".format(student.StudID, student.Name, student.StudType, student.SkillArea, student.NoOfSub, student.Result))

                    result = input("Result: ")

                    if validate_result(result, student.StudType):
                        student.Result = result

                        write_file("STUDENT.txt", students)

                        print("Result updated")
                        print("{0:6s} {1:12s} {2:8s} {3:12s} {4:7s} {5:6s}".format("StudID", "Name", "StudType", "SkillArea", "NoOfSub", "Result"))
                        print("{0:6s} {1:12s} {2:8s} {3:12s} {4:7s} {5:6s}".format(student.StudID, student.Name, student.StudType, student.SkillArea, student.NoOfSub, student.Result))

                        run = input("Continue? (Y/N) ")
                        
                    else: # invalid result
                        run = input("Invalid result format. Try again? (Y/N) ")
                    
            if not found: # StudID not found
                run = input("Student not found. Try again? (Y/N) ")

        else: # invalid studid
            run = input("Invalid StudID format. Try again? (Y/N) ")

    print("End")

# testing
# enter_result()
