# -*- coding: utf-8 -*-
def printMenu():
    print("1: Insert")
    print("2: Lookup")
    print("3: Exit program")

def exit1():
    exit

def insertLIST(sla_upp,beskrivning):
    """Nedanför läses ett ord och en beskrivning in sedan läggs
    de till i var sin lista följt av att funktionen kör igen."""
    word_to_insert = raw_input("Word to insert: ")
    if word_to_insert in sla_upp:
        print("The word is already in dictionary.")
        ordlistaLIST(sla_upp,beskrivning)
    else:
        sla_upp.append(word_to_insert)
        description_of_word = raw_input("Description of word: ")
        beskrivning.append(description_of_word)
        ordlistaLIST(sla_upp,beskrivning)

def lookupLIST(sla_upp,beskrivning):
    """Här läses ett ord in följt av att det sker en check ifall
    det ordet finns i ordlistan. Finns ordet i ordlistan skrivs
    det ut tillsammans med sin beskrivning"""
    word_to_lookup = raw_input("Word to lookup: ")
    if word_to_lookup in sla_upp:
        for n in range(len(sla_upp)):
            if word_to_lookup == sla_upp[n]:
                print("Description for "+sla_upp[n]+ ": "+ beskrivning[n])
                ordlistaLIST(sla_upp,beskrivning)
    else:
        print("That item is not in the dictionary")
        ordlistaLIST(sla_upp,beskrivning)

def ordlistaLIST(sla_upp=0, beskrivning=0):
    """En funktion som hanterar en ordlista igenom att ta in två listor en
    som fylls med ord och en annan som fylls med beskrivningar. """
    if sla_upp == 0:
        sla_upp = [] #En lista där ord till en ordlista ska skapas
        beskrivning = [] #En lista där beskrivningar till ord ska skapas
    printMenu()
    while True:
        try:
            choice = int(raw_input("Choose alternative: "))
            break
        except ValueError:
            print("Please choose option 1,2 or 3.")
            printMenu()
    if choice == 1:
        insertLIST(sla_upp,beskrivning)

    elif  choice == 2:
        lookupLIST(sla_upp,beskrivning)

    elif choice == 3:
        exit1()

    else:
        print("Please choose option 1,2 or 3.")
        ordlistaLIST(sla_upp,beskrivning)

def insertTUPLE(tuplelist):
    """Här läses ett ord och en beskrivning in som sedan sätts in i tuplelist
    i form av ett tuplepar (ord, beskrivning)"""
    word_to_insert = raw_input("Word to insert: ")
    word_in_dict = False
    for n in range(len(tuplelist)):
        if word_to_insert == tuplelist[n][0]:
            word_in_dict = True
            print("The word is already in the dictionary.")
            ordlistaTUPLE(tuplelist)
    if word_in_dict == False:
        description_of_word = raw_input("Description of word: ")
        tuplelist.append((word_to_insert,description_of_word))
        ordlistaTUPLE(tuplelist)
def lookupTUPLE(tuplelist):
    """Här läses ett ord in. Sedan letas tuplelist igenom för att kolla
    om ordet finns i listan. Finns det skrivs ordet ut tillsammans med en
    beskrivning. Annars körs funktionen igen"""
    word_to_lookup = raw_input("Word to lookup: ")
    word_found = False
    for n in range(len(tuplelist)):
        if word_to_lookup == tuplelist[n][0]:
            word_found = True
            print("Description for "+tuplelist[n][0]+ ": "+ tuplelist[n][1])
            ordlistaTUPLE(tuplelist)
    if word_found == False:
            print("That item is not in the dictionary")
            ordlistaTUPLE(tuplelist)

def ordlistaTUPLE(tuplelist=0):
    """En funktion som hanterar en ordlista igenom att ta in en lista
    som sedan fylls med tuples som består av ett ord och en beskrivning."""
    if tuplelist == 0:
        tuplelist = []
    printMenu()
    while True:
        try:
            choice = int(raw_input("Choose alternative: "))
            break
        except ValueError:
            print("Please choose option 1,2 or 3.")
            printMenu()
    if choice == 1:
        insertTUPLE(tuplelist)
    elif  choice == 2:
        lookupTUPLE(tuplelist)
    elif choice == 3:
        exit1()
    else:
        print("Please choose option 1,2 or 3.")
        ordlistaTUPLE(tuplelist)

def insertDICT(dictionary):
    """Här läses ett ord och en beskrivning in följt av att de sätts in i
    en dictionary som {ord:beskrivning}"""
    word_to_insert = raw_input("Word to insert: ")
    word_in_dict = False
    for n in range(len(dictionary)):
        if word_to_insert == dictionary.keys()[n]:
            word_in_dict = True
            print("The word is already in the dictionary.")
            ordlistaDICT(dictionary)
    if word_in_dict == False:
        description_of_word = raw_input("Description of word: ")
        dictionary[word_to_insert] = description_of_word
        ordlistaDICT(dictionary)
def lookupDICT(dictionary):
    """Nedanför läses ett ord in följt av att dictionary söks igenom i jakt
    på det inlästa ordet. Finns det skrivs det ut tillsammans med en
    beskrivning."""
    word_to_lookup = raw_input("Word to lookup: ")
    word_found = False
    for n in range(len(dictionary)):
        if word_to_lookup == dictionary.keys()[n]:
            word_found = True
            print("Description for "+dictionary.keys()[n]+ ": "+ dictionary.values()[n])
            ordlistaDICT(dictionary)
    if word_found == False:
            print("That item is not in the dictionary")
            ordlistaDICT(dictionary)

def ordlistaDICT(dictionary=0):
    """En funktion som hanterar en ordlista som tar in en dictionary
    och fyller den med ord(som nyckel) och beskrivningar(som värden)"""
    if dictionary == 0:
        dictionary = {}
    printMenu()
    while True:
        try:
            choice = int(raw_input("Choose alternative: "))
            break
        except ValueError:
            print("Please choose option 1,2 or 3.")
            printMenu()
    if choice == 1:
        insertDICT(dictionary)
    elif  choice == 2:
        lookupDICT(dictionary)
    elif choice == 3:
        exit1()
    else:
        print("Please choose option 1,2 or 3.")
        ordlistaDICT(dictionary)

ordlistaLIST()
#ordlistaTUPLE()
#ordlistaDICT()
