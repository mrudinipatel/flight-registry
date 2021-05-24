#Created by Mrudini Patel 24/05/2021

class Flight():
  def __init__ (self, capacity):
    self.capacity = capacity
    self.passengers = []

  def add_passenger(self, name):
    if not self.open_seats(): #if no seats available
      return False
    else:
      self.passengers.append(name) #add names to end of registry list
      return True

  def open_seats(self): #calculate number of open seats
    return self.capacity - len(self.passengers)

flight = Flight(4) #flight seat capacity is 4
print("There is 4 seat capacity in the flight.")
print("Please note all passengers will be registered on a first-come-first-serve basis.\n")

#asking user for names of flight attendents
people = []
people = [item for item in input("Enter the names (separated by spaces): ").split()]
#print(people)

#messages to user
print("\n")
for person in people:
  if flight.add_passenger(person):
    print(f"Added {person} to flight successfully.\n")
  else:
    print(f"No available seats for {person}\n")
 
