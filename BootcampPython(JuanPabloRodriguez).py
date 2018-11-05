import time


class Contacto:

    def __init__(self, name, last_name, age, phone_number, email):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.phone_number = phone_number
        self.email = email
        self.date = time.ctime()

    def __repr__(self):
        return '{} {} {} {} {}'.format(self.name,
                                 self.last_name,
                                 self.age,
                                 self.phone_number,
                                 self.email)

c1 = Contacto("juan", "restrepo", 22, "3204567543", "juan@globant.com")
time.sleep(2)
c2 = Contacto("Carlos", "Lopez", 20, "3164783421", "carlos@globant.com")
time.sleep(2)
c3 = Contacto("Lina", "Pulido", 30, "3005673212", "lina@globant.com")

l_contacts = []
l_contacts.append(c1)
l_contacts.append(c2)
l_contacts.append(c3)

print(l_contacts[0].name)
print(l_contacts[0].date)
print(l_contacts[1].name)
print(l_contacts[1].date)
print(l_contacts[2].name)
print(l_contacts[2].date)



def menu():
    print("Contacts App \n"
          "1. List contacts (sorted by creation date) \n"
          "2. Create new contact \n"
          "3. Update existing contact \n"
          "4. Hide contact \n \n"
          "Please enter the number... \n")
    choice = input()

    if(choice == "1"):
        l_contacts.sort(key=lambda x: x.date, reverse=False)
        for i in l_contacts:
            print(i.__repr__())
        menu()





#comprehension_list = [ e**2 for e in l_contacts if e.name]

menu()