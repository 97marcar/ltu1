sla_upp = ["123","bok","stor"]
beskrivning = ["123","sak","liten"]

def ordlista(sla_upp, beskrivning):
    print("1: Insert")
    print("2: Lookup")
    print("3: Exit program")
    choice = int(input("Choose alternative: "))
    if choice == 1:
        word_to_insert = raw_input("Word to insert: ")
        print(word_to_insert)
        sla_upp.append(word_to_insert)
        description_of_word = raw_input("Description of word: ")
        beskrivning.append(description_of_word)
        ordlista(sla_upp,beskrivning)
    elif  choice == 2:
        index = ""
        word_to_lookup = raw_input("Word to lookup: ")
        if word_to_lookup in sla_upp:
            for n in range(len(sla_upp)):
                if word_to_lookup == sla_upp[n]:
                    index = n
                    print("Description for "+sla_upp[index]+ ": "+ beskrivning[index])
                    ordlista(sla_upp,beskrivning)
        else:
            print("That item is not in the dictionary")
            ordlista(sla_upp,beskrivning)

    elif choice == 3:
        return
    else:
        print("Please choose option 1,2 or 3.")

ordlista(sla_upp,beskrivning)
