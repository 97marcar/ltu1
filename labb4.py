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
        print('Enter "change [name] [number]" to edit a contact')
        print('Look up numbers: "lookup [name]"')
        print('Load file "load [filename](not including .csv)"')
        print('Save file "save [filename]"(not including .csv)')
        print('Type "exit" to exit.\n')
        self.command()

    def command(self):
        while True:
            try:
                theInput = raw_input(">>> ").strip()
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
            if givenCommand == "exit":
                return
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
            self.phonebook.append([name,"",number])
            print('"A person with the name: "'+name+'" and number: "'+\
            number+'" entered successfully.')
            self.command()
        else:
            print("A person with that phonenumber already exists.")
            self.command()
    def change(self,name, newnum, currentnum=False):
        self.countSameNames(name)
        if self.countSameNames == 1:
            for n in range(len(self.phonebook)):
                if self.phonebook[n][0] == name:
                    self.phonebook[n][2] = newnum
                    print("Number changed")
                    self.command()
                    return

        elif self.countSameNames > 1 and currentnum == False:
            print("There a multiple contacts by that name.")
            print('To change please write "change [name] [newnumber] [oldnumber]"')
            self.command()
            return

        elif self.countSameNames > 1 and currentnum != False:
            for n in range(len(self.phonebook)):
                if self.phonebook[n][0] == name and self.phonebook[n][2] == currentnum:
                    self.phonebook[n][2] = newnum
                    print("Number changed")
                    self.command()
                    return
            print('There is no contact with that name and number.')
            self.command()
            return

        print('There is no contact by that name.')
        self.command()


    def lookup(self, name):
        for n in range(len(self.phonebook)):
            if self.phonebook[n][0] == name:
                print(self.phonebook[n][2])

            else:
                print("The name is not in the phonebook.")

        self.command()


    def save(self,name):
        with open(name+".csv","wb") as csvfile:
            write = csv.writer(csvfile, delimiter=';')
            write.writerow(self.phonebook[0])
            write.writerow(self.phonebook[1])

    def countSameNames(self, name):
        self.numberOfNames = 0
        for n in range(len(self.phonebook)):
            if self.phonebook[n][0] == name:
                self.numberOfNames += 1

    def searchForSameNumber(self, number):
        for n in range(len(self.phonebook)):
            print(self.phonebook[n][2])
            if self.phonebook[n][2] == number:
                self.bool1 = False
                return
            else:
                self.bool1 = True


Telefonbok()
