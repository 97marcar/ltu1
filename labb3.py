# -*- coding: utf-8 -*-
def printMenu():
    print("1: Insert")
    print("2: Lookup")
    print("3: Exit program")

sla_upp = [] #En lista där ord till en ordlista ska skapas
beskrivning = [] #En lista där beskrivningar till ord ska skapas

def ordlistaLIST(sla_upp, beskrivning):
    """En funktion som hanterar en ordlista igenom att ta in två listor en
    som fylls med ord och en annan som fylls med beskrivningar. """
    printMenu()
    choice = int(input("Choose alternative: "))
    if choice == 1:
        #Nedanför läses ett ord och en beskrivning in sedan läggs
        #de till i var sin lista följt av att funktionen kör igen.
        word_to_insert = raw_input("Word to insert: ")
        sla_upp.append(word_to_insert)
        description_of_word = raw_input("Description of word: ")
        beskrivning.append(description_of_word)
        ordlistaLIST(sla_upp,beskrivning)
    elif  choice == 2:
        #Här läses ett ord in följt av att det sker en check ifall
        #det ordet finns i ordlistan. Finns ordet i ordlistan skrivs
        #det ut tillsammans med sin beskrivning
        word_to_lookup = raw_input("Word to lookup: ")
        if word_to_lookup in sla_upp:
            for n in range(len(sla_upp)):
                if word_to_lookup == sla_upp[n]:
                    print("Description for "+sla_upp[n]+ ": "+ beskrivning[n])
                    ordlistaLIST(sla_upp,beskrivning)
        else:
            print("That item is not in the dictionary")
            ordlistaLIST(sla_upp,beskrivning)

    elif choice == 3:
        #return gör att funktionen slutar köra
        return
    else:
        print("Please choose option 1,2 or 3.")

tuplelist = []
def ordlistaTUPLE(tuplelist):
    """En funktion som hanterar en ordlista igenom att ta in en lista
    som sedan fylls med tuples som består av ett ord och en beskrivning."""
    printMenu()
    choice = int(input("Choose alternative: "))
    if choice == 1:
        #Här läses ett ord och en beskrivning in som sedan sätts in i tuplelist
        #i form av ett tuplepar (ord, beskrivning)
        word_to_insert = raw_input("Word to insert: ")
        description_of_word = raw_input("Description of word: ")
        tuplelist.append((word_to_insert,description_of_word))
        ordlistaTUPLE(tuplelist)
    elif  choice == 2:
        #Nedanför läses ett ord in. Sedan letas tuplelist igenom för att kolla
        #om ordet finns i listan. Finns det skrivs ordet ut tillsammans med en
        #beskrivning. Annars körs funktionen igen
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
    elif choice == 3:
        return
    else:
        print("Please choose option 1,2 or 3.")
        ordlistaTUPLE(tuplelist)

dictionary = {}
def ordlistaDICT(dictionary):
    """En funktion som hanterar en ordlista som tar in en dictionary
    och fyller den med ord(som nyckel) och beskrivningar(som värden)"""
    printMenu()
    choice = int(input("Choose alternative: "))
    if choice == 1:
        #Här läses ett ord och en beskrivning in följt av att de sätts in i
        #en dictionary som {ord:beskrivning}
        word_to_insert = raw_input("Word to insert: ")
        description_of_word = raw_input("Description of word: ")
        dictionary[word_to_insert] = description_of_word
        ordlistaDICT(dictionary)
    elif  choice == 2:
        #Nedanför läses ett ord in följt av att dictionary söks igenom i jakt
        #på det inlästa ordet. Finns det skrivs det ut tillsammans med en
        #beskrivning.
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
    elif choice == 3:
        return
    else:
        print("Please choose option 1,2 or 3.")
        ordlistaDICT(dictionary)

#ordlistaTUPLE(tuplelist)
#ordlistaLIST(sla_upp,beskrivning)
ordlistaDICT(dictionary)
