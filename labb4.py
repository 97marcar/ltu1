
class Telefonbok():
    def __init__(self):
        self.phonebook = []
        self.mainMenu()
        self.mainOption()

    def mainMenu(self):
        print("\nTelephone book")
        print("Main Menu")
        print("Please choose one option below: ")
        print("1. Add.
        print("2. Create/change alias or change number.")
        print("2. Look up a name in the phonebook.")
        print("3. Load/Save")
        print("4. Exit\n")

    def mainOption(self):
        while True:
            try:
                choice = int(input(">>> "))
                break
            except ValueError:
                print("Input one of the options above.")
        if choice == 1:
            self.addMenu()
        elif choice == 2:
            self.lookupMenu()
        elif choice == 3:
            self.loadsaveMenu()
        elif choice == 4:
            exit


        print('"lookup [name] [number]" to look up a contact')
        print('"alias [name] [alias]" to create an alias for a contact\n')

    def addMenu(self):
        print("Add menu")
        print('Enter "add [name] [number]" to add a contact')
        self.threeOption("add")

    def threeOption(self, origin):
        while True:
            try:
                givenOption, name, number = raw_input(">>> ").split(" ")
                break
            except ValueError:
                print("\nError. Make sure that the format is correct.\n")

        print(givenOption + " " + name + " " + number)
        if givenOption, origin == "add":
            self.add(name, number)
        elif givenOption == "quit":
            return

    def add(self, name, number):
        self.phonebook.append([name,"",number])
        self.phonebook[0][1] = "rune"
        print(self.phonebook)
        print(self.phonebook[0][0])
        self.option()

    def searchForSameNumber(self, number):
        for n in len(self.phonebook):
            if self.phonebook[n][2] == number:
                return False


Telefonbok()
