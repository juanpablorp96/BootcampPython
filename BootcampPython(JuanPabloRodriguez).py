

class Contacto:

    def __init__(self, name, Last_name, age, Phone_number, email):
        self.name = name
        self.Last_name = Last_name
        self.age = age
        self.Phone_number = Phone_number
        self.email = email

c = Contacto("juan", "restrepo", 22, 3204567543, "juan@globant.com")

c.nuevo_atr = 320493534
c.age = 30

print(c.age)