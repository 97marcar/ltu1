import csv
class Telefonbok():
    def __init__(self):
        self.bool1 = True
        self.numberOfNames = 0
        self.phonebook = []
        self.mainMenu()

    def mainMenu(self):
        print("\nTelephone book")
        print("Main Menu")
        print("Following commands exists: ")
        print('Enter "add [name] [number]" to add a contact')
        print('Enter "remove [name] [number]" to remove a contact')
        print('Enter "change [name] [newnumber]" to edit a contact')
        print('Look up numbers: "lookup [name]"')
        print('Load file "load [filename](not including .csv)"')
        print('Save file "save [filename]"(not including .csv)')
        print('Type "mainmenu" to show this menu again.')
        print('Type "quit" to quit.\n')
        self.command()

    def command(self):
        while True:
            try:
                theInput = raw_input(">>> ").strip()
                print(self.phonebook)
                print(theInput)
                spaces = theInput.count(" ")
                if ";" in theInput:
                    print('The symbol ";" is not allowed')
                    spaces = 666
                    self.command()

                if spaces == 0:
                    givenCommand = theInput
                    break
                elif spaces == 1:
                    givenCommand, arg1 = theInput.split()
                    break
                elif spaces == 2:
                    givenCommand, arg1, arg2 = theInput.split()
                    break
                elif spaces == 3:
                    givenCommand, arg1, arg2, arg3 = theInput.split()
                    break
                elif spaces == 666:
                    pass
                else:
                    print("Please enter a valid command.")
            except:
                print("Error")

        if spaces == 0:
            if givenCommand == "quit":
                return
            elif givenCommand == "mainmenu":
                self.mainMenu()
            else:
                print("Please enter a valid command.")
                self.command()

        elif spaces == 1:
            if givenCommand == "lookup":
                self.lookup(arg1)
            elif givenCommand == "save":
                self.save(arg1)
            elif givenCommand == "load":
                self.load(arg1)
            else:
                print("Please enter a valid command.")
                self.command()

        elif spaces == 2:
            if givenCommand == "add":
                self.add(arg1,arg2)
            elif givenCommand == "remove":
                self.remove(arg1,arg2)
            elif givenCommand == "alias":
                self.alias(arg1, arg2)
            elif givenCommand == "change":
                self.change(arg1,arg2)
            else:
                print("Please enter a valid command.")
                self.command()

        elif spaces == 3:
            if givenCommand == "alias":
                self.alias(arg1, arg2, arg3)
            elif givenCommand == "change":
                self.change(arg1, arg2, arg3)
            else:
                print("Please enter a valid command.")
                self.command()

        else:
            print("Please enter a valid command.")
            self.command()

    def add(self, name, number):
        self.searchForSameNumber(number)
        if self.bool1 == True:
            self.phonebook.append([number,name])
            print('"A person with the name: "'+name+'" and number: "'+\
            number+'" entered successfully.')
            self.command()
        else:
            print("A person with that phonenumber already exists.")
            self.command()

    def alias(self,name, alias, number=False):
        self.countSameNames(name)
        if self.numberOfNames == 1:
            for n in range(len(self.phonebook)):
                if name in self.phonebook[n] and name != self.phonebook[n][0]:
                    self.phonebook[n].append(alias)
                    print("Alias added.")
                    self.command()
                    return
        elif self.numberOfNames > 1 and number == False:
            print("There are multiple contacts by that name.")
            print('To add alias please write "alias [name] [alias] [number]"')
            self.command()
            return
        elif self.numberOfNames > 1 and number != False:
            for n in range(len(self.phonebook)):
                if (name in self.phonebook[n] and name != self.phonebook[n][0]) and self.phonebook[n][0] == number:
                    self.phonebook[n].append(alias)
                    print("Alias added/edited.")
                    self.command()
                    return
            print('There is no contact with that name and number.')
            self.command()
            return

        print('There is no contact by that name.')
        self.command()

    def change(self,name, newnum, currentnum=False):
        self.countSameNames(name)
        if self.numberOfNames == 1:
            for n in range(len(self.phonebook)):
                if name in self.phonebook[n] and name != self.phonebook[n][0]:
                    self.phonebook[n][0] = newnum
                    print("Number changed")
                    self.command()
                    return

        elif self.numberOfNames > 1 and currentnum == False:
            print("There a multiple contacts by that name.")
            print('To change please write "change [name] [newnumber] [oldnumber]"')
            self.command()
            return

        elif self.numberOfNames > 1 and currentnum != False:
            for n in range(len(self.phonebook)):
                if (name in self.phonebook[n] and name != self.phonebook[n][0]) and self.phonebook[n][0] == currentnum:
                    self.phonebook[n][0] = newnum
                    print("Number changed")
                    self.command()
                    return
            print('There is no contact with that name and number.')
            self.command()
            return

        print('There is no contact by that name.')
        self.command()

    def remove(self,name,number):
        for n in range(len(self.phonebook)):
            if name in self.phonebook[n] and name != self.phonebook[n][0]:
                del self.phonebook[n]
                print("Removed.")
                self.command()

    def lookup(self, name):
        self.countSameNames(name)
        if self.numberOfNames == 0:
            print("The name is not in the phonebook.")
            self.command()
        else:
            for n in range(len(self.phonebook)):
                if name in self.phonebook[n] and name != self.phonebook[n][0]:
                    print(self.phonebook[n][0])

            self.command()
            return



    def save(self,name):
        with open(name+".csv","wb") as csvfile:
            write = csv.writer(csvfile, delimiter=';')
            for n in range(len(self.phonebook)):
                write.writerow(self.phonebook[n])
        self.command()

    def load(self,name):
        self.phonebook = []
        try:
            with open(name+".csv", "rb") as csvfile:
                read = csv.reader(csvfile, delimiter=';')
                for row in read:
                    self.phonebook.append(row)
            self.command()
        except:
            print("There is no file by that name.")
            self.command()

    def countSameNames(self, name):
        self.numberOfNames = 0
        for n in range(len(self.phonebook)):
            if name in self.phonebook[n] and name != self.phonebook[n][0]:
                self.numberOfNames += 1

    def searchForSameNumber(self, number):
        for n in range(len(self.phonebook)):
            if self.phonebook[n][0] == number:
                self.bool1 = False
                return
            else:
                self.bool1 = True


Telefonbok()
