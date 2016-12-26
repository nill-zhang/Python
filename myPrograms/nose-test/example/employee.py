class Employee(object):
    ''' a  class about company employees'''

    compay = "SFZHANG.INC"
  
    def __init__(self, name, age, salary, office, height, employeeid):
        self.name = name
        self.salary = salary
        self.age = age
        self.office = office
        self.employeeid = employeeid
        self.height = height
        self.ranking = ''
        self.skills = []
        self.attendance = {}
    
    def get_ranking(self):
        if self.employeeid < 1000:
            self.ranking = 'junior'
        elif self.employeeid < 2000:
            self.ranking = 'intermediate'
        else:
            self.ranking = 'senior'
        

    def origin(self, country):
        if country !=  "Canada":
            return "international"
        else:
            return "citizen"

    def add_skills(self,skill):
        self.skills.extend(skill)

    def add_attendance(self,attendance):
        self.attendance.update(attendance)

    def get_attendance(self):
       return sum(i for i in  self.attendance.values())
            
