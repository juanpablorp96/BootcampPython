import time


class Contacto:

    def __init__(self, name, last_name, age, email, phone_number):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.phone_number = phone_number
        self.date = time.ctime()

    def __repr__(self):
        return '{} {} {} {} {}'.format(self.name,
                                 self.last_name,
                                 self.age,
                                 self.email,
                                 self.phone_number)



l_contacts = []
l_contacts.append(Contacto("juan", "restrepo", 22, "juan@globant.com", {"house": "3542134", "cell phone": "3204532478"}))
time.sleep(2)
l_contacts.append(Contacto("Carlos", "Lopez", 20, "carlos@globant.com", {"office": "2345673", "cell phone": "3156385721"}))
time.sleep(2)
l_contacts.append(Contacto("Lina", "Pulido", 30, "lina@globant.com", {"personal": "1234567", "cell phone": "3005732146"}))

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
          "Please enter the number...")
    choice = input()

    if(choice == "1"):
        l_contacts.sort(key=lambda x: x.date, reverse=False)
        for i in l_contacts:
            print(i.__repr__())
        menu()

    if(choice == "2"):
        print("Enter name:")
        name = input()
        print("Enter last name:")
        last_name = input()
        print("Enter age:")
        age = input()
        print("Enter email:")
        email = input()
        print("Enter phone number name (office, personal, cell phone, etc): \n")
        phone_number_name = input()
        print("Enter phone number for " + phone_number_name)
        phone_number = input()

        l_contacts.append(Contacto(name, last_name, int(age), email, {phone_number_name: phone_number}))
        flag = True

        while(flag == True):
            print("Other phone number? \n 1. Yes  2. No")
            choice = input()
            if(choice == "1"):
                print("Enter phone number name (office, personal, cell phone, etc): \n")
                phone_number_name = input()
                print("Enter phone number for " + phone_number_name)
                phone_number = input()
                l_contacts[len(l_contacts) - 1].phone_number[phone_number_name] = phone_number

            if(choice == "2"):
                flag = False

        menu()




#comprehension_list = [ e**2 for e in l_contacts if e.name]

menu()