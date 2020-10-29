#!python3

"""
Create a class that will store a database for a veterinarian.
Your class will need the following properties:

animal (dog, cat, fish, bird, turtle, etc)
breed
name (the pet's name)
owner (the owner's name)
birthdate (of the pet, expressed as yyyy-mm-dd)

The constructor will need to ask for each of those values
for the database when the pet is instantiated

Methods:
display() - should show the name of the pet and type followed by their breed and owner


Main block should have a menu that has the following options:
1. Enter a new pet
2. Retrieve a pet
3. Exit

If they choose to retrieve a pet,
display the following:
Enter pet's name:
and then go through the list, looking for the name of the pet.
If the pet is found, it should call the display() method from the object

Example output:
1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? cat
Breed? Domestic Long Hair
Name? Benjamin
Owner? Chris
Birthdate? 20015-10-01

1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? dog
Breed? Shih-tzu
Name? Buster
Owner? Christy
Birthdate? 2008-10-16

1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? cat
Breed? Domestic Long Hair
Name? Casey
Owner? Chris
Birthdate? 20015-10-01

1. Enter a new pet
2. Retrieve a pet
3. Exit
2

Which Pet? Buster

Buster dog
Shih-tzu is owned by Christy
(10 points) 
"""


class pet:
    animal = None
    breed = None
    name = None
    owner = None
    birthday = None

    def __init__(self):
        print("\n")
        self.animal = input("Enter the type of animal: ")
        self.breed = input("Enter the breed: ")
        self.name = input("Enter the name: ")
        self.owner = input("Enter the owner: ")
        self.birthday = input("Enter the birthday: ")

    def display(self):
        output = str(self.name) + " " + str(self.animal) + " " + str(self.breed) + " is owned by " + str(self.owner)
        outputLength = len(output)
        print(outputLength * "=")
        print(output)
        print(outputLength * "=")
        
    
def main():
    quitbool = 0
    while quitbool != 3:
        print("\n1.Enter a new pet\n2.Retrieve a pet\n3.Exit")
        quitbool = int(input(""))
        if quitbool == 1:
            pets = []
            for i in range(0,3):
                pets.append(pet())
        elif quitbool == 2:
            namebool = input("Which Pet?")
            if namebool == pets[0].name:
                pets[0].display()
            elif namebool == pets[1].name:
                pets[1].display()
            elif namebool == pets[2].name:
                pets[2].display()



main()

            
