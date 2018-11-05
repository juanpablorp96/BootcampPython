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
l_hidden = []
l_contacts.append(Contacto("juan", "restrepo", 22, "juan@globant.com", {"house": "3542134", "cell phone": "3204532478"}))
time.sleep(2)
l_contacts.append(Contacto("Carlos", "Lopez", 20, "carlos@globant.com", {"office": "2345673", "cell phone": "3156385721"}))
time.sleep(2)
l_contacts.append(Contacto("Lina", "Pulido", 30, "lina@globant.com", {"personal": "1234567", "cell phone": "3005732146"}))


def menu():
    print("Contacts App \n"
          "1. List contacts (sorted by creation date) \n"
          "2. Create new contact \n"
          "3. Update existing contact \n"
          "4. Hide contact \n"
          "5. Recover hidden contacts \n \n"
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

    if(choice == "3"):
        count = 1
        print("Choose contact")
        for i in l_contacts:
            print('{}. {}'.format(count, i.__repr__()))
            count += 1
        contact_update = input()

        print("Choose option to update \n 1. Name \n 2. Last Name \n 3. Age \n 4. Email \n 5. Numbers")
        choice = input()

        if(choice == "1"):
            print('Current name --> {}'.format(l_contacts[int(contact_update) - 1].name))
            print("Enter new name")
            new_name = input()
            l_contacts[int(contact_update) - 1].name = new_name
            print("Successful update")

        if(choice == "2"):
            print('Current last name --> {}'.format(l_contacts[int(contact_update) - 1].last_name))
            print("Enter new last name")
            new_last_name = input()
            l_contacts[int(contact_update) - 1].last_name = new_last_name
            print("Successful update")


        if(choice == "3"):
            print('Current age --> {}'.format(l_contacts[int(contact_update) - 1].age))
            print("Enter new age")
            new_age = input()
            l_contacts[int(contact_update) - 1].age = int(new_age)
            print("Successful update")


        if(choice == "4"):
            print('Current email --> {}'.format(l_contacts[int(contact_update) - 1].email))
            print("Enter new email")
            new_email = input()
            l_contacts[int(contact_update) - 1].email = new_email
            print("Successful update")

        if(choice == "5"):
            count = 1
            print("Current numbers: \n")
            for key, val in l_contacts[int(contact_update) - 1].phone_number.items():
                print('{}. {}: {}'.format(count, key, val))
                count += 1
            print("Choose a number")
            num = input()
            count = 1
            for key in l_contacts[int(contact_update) - 1].phone_number:
                if(int(num) == count):
                    print("Enter new phone number")
                    new_phone_number = input()
                    l_contacts[int(contact_update) - 1].phone_number[key] = new_phone_number
                count += 1
        menu()

    if(choice == "4"):
        count = 1
        print("Choose contact")
        for i in l_contacts:
            print('{}. {}'.format(count, i.__repr__()))
            count += 1
        hide_contact = input()
        l_hidden.append(l_contacts.pop(int(hide_contact) - 1))
        print("Successful hide \n")

        menu()

    if(choice == "5"):
        for i in l_hidden:
            l_contacts.append(i)
        print("Successful recover of hidden contacts")

        menu()

#comprehension_list = [ e**2 for e in l_contacts if e.name]

menu()