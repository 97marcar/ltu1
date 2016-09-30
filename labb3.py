sla_upp = []
beskrivning = []

def ordlistaLIST(sla_upp, beskrivning):
    print("1: Insert")
    print("2: Lookup")
    print("3: Exit program")
    choice = int(input("Choose alternative: "))
    if choice == 1:
        word_to_insert = raw_input("Word to insert: ")
        sla_upp.append(word_to_insert)
        description_of_word = raw_input("Description of word: ")
        beskrivning.append(description_of_word)
        ordlistaLIST(sla_upp,beskrivning)
    elif  choice == 2:
        index = ""
        word_to_lookup = raw_input("Word to lookup: ")
        if word_to_lookup in sla_upp:
            for n in range(len(sla_upp)):
                if word_to_lookup == sla_upp[n]:
                    index = n
                    print("Description for "+sla_upp[index]+ ": "+ beskrivning[index])
                    ordlistaLIST(sla_upp,beskrivning)
        else:
            print("That item is not in the dictionary")
            ordlistaLIST(sla_upp,beskrivning)

    elif choice == 3:
        return
    else:
        print("Please choose option 1,2 or 3.")

tuplelist = []
def ordlistaTUPLE(tuplelist):
    print("1: Insert")
    print("2: Lookup")
    print("3: Exit program")
    choice = int(input("Choose alternative: "))
    if choice == 1:
        word_to_insert = raw_input("Word to insert: ")
        description_of_word = raw_input("Description of word: ")
        tuplelist.append((word_to_insert,description_of_word))
        ordlistaTUPLE(tuplelist)
    elif  choice == 2:
        index = ""
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
    print("1: Insert")
    print("2: Lookup")
    print("3: Exit program")
    choice = int(input("Choose alternative: "))
    if choice == 1:
        word_to_insert = raw_input("Word to insert: ")
        description_of_word = raw_input("Description of word: ")
        dictionary[word_to_insert] = description_of_word
        ordlistaDICT(dictionary)
    elif  choice == 2:
        index = ""
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
