# You’ve started a position as the lead programmer for the family-style Italian restaurant Basta Fazoolin’ with My Heart. 
# The restaurant has been doing fantastically and seen a lot of growth lately. 
# You’ve been hired to keep things organized.

# classes
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__ (self):
    return self.name + ' available from ' + str(self.start_time) + ' to ' + str(self.end_time)

  def calculate_bill(self, purchased_items):
    bill = 0
    for item in purchased_items:
      if item in self.items:
        bill += self.items[item] 
    return bill 


class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  
  def __repr__(self):
    return "Restaurant address: " + self.address

  def available_menus(self, time):
    available = []
    for menu in self.menus:
      if menu.start_time >= time and menu.end_time >= time:
        available.append(menu)
    
    return available

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises


# lists of items
brunch = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

early_bird = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

dinner = {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

kids = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

arepas = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

# menus
brunch_menu = Menu("branch menu", brunch, 1100, 16000)
early_bird_menu = Menu("early bird menu", early_bird, 1500, 1800)
dinner_menu = Menu("dinner menu",dinner, 1700, 2300)
kids_menu = Menu("kids menu ", kids, 1100, 2100)
arepa_menu = Menu("Arepa menu pendejo", arepas, 1000, 2000)
all_menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu, arepa_menu]

# check section
print(kids_menu)
print(kids_menu.calculate_bill(kids))
print(early_bird_menu.calculate_bill(early_bird))

# franchises instances
flagship_store = Franchise("1232 West End Road", all_menus)
new_installment = Franchise("12 East Mulberry Street", all_menus)
all_franchises = [flagship_store, new_installment]

# check section 2
print(flagship_store)
print(flagship_store.available_menus(1200))
print(flagship_store.available_menus(1700))

# business
first_business = Business("Basta Fazoolin' with my Heart", all_franchises)

arepas_place = Franchise("189 Fitzgerald Avenue", arepa_menu)
arepa_business = Business("Take a' Arepa", arepas_place)