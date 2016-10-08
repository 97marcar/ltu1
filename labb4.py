
class Telefonbok():
    def __init__(self):
        self.phonebook = []
        self.mainMenu()

    def mainMenu(self):
        print("\nTelephone book")
        print("Main Menu")
        print("Please choose one option below: ")
        print("1. Add/remove.")
        print("2. Create/change alias or change number.")
        print("3. Look up a name in the phonebook.")
        print("4. Load/Save.")
        print("5. Exit.\n")
        self.mainOption()

    def mainOption(self):
        while True:
            try:
                choice = int(input(">>> "))
                break
            except SyntaxError:
                self.mainMenu()
                print("Input one of the options above.")
            except NameError:
                self.mainMenu()
                print("Input one of the options above.")
        if choice == 1:
            self.addMenu()
        elif choice == 2:
            self.aliasMenu()
        elif choice == 3:
            self.lookupMenu()
        elif choice == 4:
            self.loadsaveMenu()
        elif choice == 5:
            exit
        else:
            self.mainMenu()
            print("Input one of the options above.")
            self.mainOption()


        print('"lookup [name] [number]" to look up a contact')
        print('"alias [name] [alias]" to create an alias for a contact\n')

    def addMenu(self):
        print("\nAdd/remove menu")
        print('To add: enter "add [name] [number]" to add a contact')
        print('To remove: enter "remove [name] [number]"')
        print('If you need to exit just type "get me out"\n')
        self.threeOption("add")

    def lookupMenu(self):
        print("Look up menu")
        print('To look up numbers belonging to a name enter: lookup [name]')
        print('If you need to exit just type "exit program"')
        self.twoOption("lookup")

    def twoOption(self, origin):
        while True:
            try:
                givenOption, name = raw_input(">>> ").split()
                break
            except ValueError and SyntaxError:
                print("\nError. Make sure that the format is correct.\n")

        if givenOption == "lookup" and origin == "lookup":
            self.lookup(name)
        elif givenOption == "exit" and name == "program":
            return
    def threeOption(self, origin):
        while True:
            try:
                givenOption, name, number = raw_input(">>> ").split()
                break
            except ValueError:
                print("\nError. Make sure that the format is correct.\n")

        print(givenOption + " " + name + " " + number)
        if givenOption == "add" and origin == "add":
            self.add(name, number)
        elif givenOption == "get" and name == "me" and number == "out":
            return

    def add(self, name, number):
        if not self.searchForSameNumber(number):
            self.phonebook.append([name,"",number])
        else:
            print("A person with that phonenumber already exists.")
            self.threeOption("add")

        print('"A person with the name: "'+name+'" and number: '+\
        number+" entered successfully.")
        self.mainMenu()

    def lookup(self, name):
        for n in range(len(self.phonebook)):
            if self.phonebook[n][0] == name:
                print("")

    def searchForSameNumber(self, number):
        print(len(self.phonebook))
        for n in range(len(self.phonebook)):
            if self.phonebook[n][2] == number:
                return False


Telefonbok()
