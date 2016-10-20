# -*- coding: utf-8 -*-
import csv

class Telefonbok():
    """En klass som innehåller en telefonbok med ett antal olika
    funktioner(lägg till, ta bort ändra mm.)"""
    def __init__(self):
        """Konstruktorn, körs när klassen först körs"""
        self.bool1 = True
        self.numberOfNames = 0
        self.phonebook = []
        self.mainMenu()

    def mainMenu(self):
        """Skriver ut menyn till användaren så han/hon enkelt kan
        se alla typer av kommandon som kan utföras"""
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
        """Hanterar inputen som sker av användaren och ser till
        att rätt funktion körs beroende på vad som skrivs in."""
        while True:
            try:
                #Tar in input från användaren och beroende
                #på hur många ord som skrivs hanteras datan
                #olika.
                theInput = raw_input(">>> ").strip()
                while '  ' in theInput:
                    theInput = theInput.replace('  ', ' ')
                print(theInput)
                spaces = theInput.count(" ")

                #Ser till att ";" inte används i namnet pga
                #load och save funktionerna
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

        #Nedan skickas data till respektive funktion
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
            elif givenCommand == "remove":
                self.remove(arg1)
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
        """Tar in ett namn och ett number som argument och
        lägger till dem i telefonboken så länge nummret inte
        är upptaget."""
        self.searchForSameNameAndNumber(name, number)
        if self.bool1 == True:
            if name != number:
                self.phonebook.append([number,name])
                print('"A person with the name: "'+name+'" and number: "'+\
                number+'" entered successfully.')
                self.command()
            else:
                print("The name cannot be the same as number.")
                self.command()

        else:
            print("A person with that phonenumber already exists.")
            self.command()

    def alias(self,name, alias, number=False):
        """Lägger till namn till de redan existerande personer i
        telefonboken. Tar in namn och alias som argument vilket räcker
        så länge det bara finns en person med samma namn annars behövs
        nummret också."""
        self.countSameNames(name)
        if self.numberOfNames == 1:
            for n in range(len(self.phonebook)):
                if self.phonebook[n][0] != alias:
                    if name in self.phonebook[n] and name != self.phonebook[n][0]:
                        self.searchForSameNameAndNumber(alias, self.phonebook[n][0])
                        if self.bool1 == True:
                            self.phonebook[n].append(alias)
                            print("Alias added.")
                            self.command()
                            return
                        else:
                            print("There is a person with that name and number.")
                            self.command()
                            return
                else:
                    print("Alias and number cannot be the same.")
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
                    self.searchForSameNameAndNumber(alias, self.phonebook[n][0])
                    if self.bool1 == True:
                        self.phonebook[n].append(alias)
                        print("Alias added.")
                        self.command()
                        return
                    else:
                        print("There is a person with that name and number.")
                        self.command()
                        return
            print('There is no contact with that name and number.')
            self.command()
            return

        print('There is no contact by that name.')
        self.command()

    def change(self,name, newnum, currentnum=False):
        """Redigerar det existerande nummret till en kontakt.
        Tar in namn och det nya telefonboken. Det räcker så länge det
        bara finns en person med samma namn annars behövs det gamla
        nummret också"""
        self.countSameNames(name)
        if self.numberOfNames == 1:
            for n in range(len(self.phonebook)):
                if name in self.phonebook[n] and name != self.phonebook[n][0]:
                    self.searchForSameNameAndNumber2(name, newnum)
                    if self.bool1 == True:
                        self.phonebook[n][0] = newnum
                        print("Number changed")
                        self.command()
                        return
                    else:
                        print("There is a person with that name and number.")
                        self.command()
                        return

        elif self.numberOfNames > 1 and currentnum == False:
            print("There a multiple contacts by that name.")
            print('To change please write "change [name] [newnumber] [oldnumber]"')
            self.command()
            return

        elif self.numberOfNames > 1 and currentnum != False:
            for n in range(len(self.phonebook)):
                print(name, newnum)
                self.searchForSameNameAndNumber2(name, currentnum)

                if self.bool1 == True:
                    if (name in self.phonebook[n] and name != self.phonebook[n][0]) and self.phonebook[n][0] == currentnum:
                        self.phonebook[n][0] = newnum
                        print("Number changed")
                        self.command()
                        return
                else:
                    print("There is a person with that name and number.")
                    self.command()
                    return
            print('There is no contact with that name and number.')
            self.command()
            return

        print('There is no contact by that name.')
        self.command()

    def remove(self,name,number=False):
        """Tar bort en kontakt från telefonboken. Tar in namn
        och nummer."""
        self.countSameNames(name)
        if self.numberOfNames == 1:
            for n in range(len(self.phonebook)):
                if name in self.phonebook[n] and name != self.phonebook[n][0]:
                    del self.phonebook[n]
                    print("Removed.")
                    self.command()
                    return
        elif self.numberOfNames > 1 and number == False:
            print("There are multiple contacts by that name.")
            print("Please write remove [name] [number]")
            self.command()
            return

        elif self.numberOfNames > 1 and number != False:
            for n in range(len(self.phonebook)):
                if (name in self.phonebook[n] and name != self.phonebook[n][0]) and self.phonebook[n][0] == number:
                    del self.phonebook[n]
                    print("Removed.")
                    self.command()
                    return
        print("There is no contact with that name and number.")
        self.command()

    def lookup(self, name):
        """Skriver ut alla nummer som tillhör ett visst namn."""
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
        """Sparar telefonboken i en csvfil med namn som väljs av
        användaren."""
        try:
            with open(name+".csv","wb") as csvfile:
                write = csv.writer(csvfile, delimiter=';')
                for n in range(len(self.phonebook)):
                    write.writerow(self.phonebook[n])
                print("File saved.")
        except:
            print("Error saving file.")
        self.command()

    def load(self,name):
        """Laddar en csvfil som innehållet en telefonbok."""

        try:
            with open(name+".csv", "rb") as csvfile:
                self.phonebook = []
                read = csv.reader(csvfile, delimiter=';')
                for row in read:
                    self.phonebook.append(row)
            self.command()
        except:
            print("There is no file by that name.")
            self.command()

    def countSameNames(self, name):
        """Räknar antalet av samma namn som finns i telefonboken."""
        self.numberOfNames = 0
        for n in range(len(self.phonebook)):
            if name in self.phonebook[n] and name != self.phonebook[n][0]:
                self.numberOfNames += 1

    def searchForSameNameAndNumber(self, name, number):
        """Kolla om ett nummer och namn finns i ordboken eller inte.
        Get en variabel värdet sant eller falsk"""
        for n in range(len(self.phonebook)):
            if name in self.phonebook[n]:
                for i in self.phonebook[n]:
                    if number in self.phonebook[n] and i in self.phonebook[n]:
                        self.bool1 = False
                        return
        self.bool1 = True

    def searchForSameNameAndNumber2(self, name, number):
        """Kolla om ett nummer och namn finns i ordboken eller inte.
        Get en variabel värdet sant eller falsk."""
        for n in range(len(self.phonebook)):
            if number in self.phonebook[n]:
                for i in self.phonebook[n]:
                    if i in self.phonebook[n]:
                        self.bool1 = False
                        return
        self.bool1 = True


Telefonbok()
