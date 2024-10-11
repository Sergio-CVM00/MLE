class School:
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents
  
  def __repr__(self):
    return "A " + self.level + " school named " + self.name + " with " + str(self.numberOfStudents) + " students"

  # setters
  def set_name(self, name):
    self.name = name
  
  def set_level(self, level):
    self.level = level
  
  def set_numberOfStudents(self, numberOfStudents):
    self.numberOfStudents = numberOfStudents
  
  # getters
  def get_name(self):
    return self.name

  def get_level(self):
    return self.level
  
  def get_numberOfStudents(self):
    return self.numberOfStudents

class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, 'primary', numberOfStudents)
    self.pickupPolicy = pickupPolicy

  def __repr__(self):
    return 'primary school named: ' + self.name + ' with No. of students: ' + str(self.numberOfStudents) + ' and with pickup Policy: ' + self.pickupPolicy

  def getPickupPolicy(self):
    return self.pickupPolicy

class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeam):
    super().__init__(name, 'high', numberOfStudents)
    self.sportsTeam = sportsTeam

  def __repr__(self):
    return 'High school named: ' + self.name + ' with No. of students: ' + str(self.numberOfStudents) + ' and with sports team: ' + self.sportsTeam

  def getSportsTeam(self):
    return self.sportsTeam


# print section to check it out
b = PrimarySchool("Codecademy", 300, "Pickup Allowed")
print(b.getPickupPolicy())
print(b)

c = HighSchool("Codecademy", 300, "Pickup Allowed")
print(c.getSportsTeam())
print(c)