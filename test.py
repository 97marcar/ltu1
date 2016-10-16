while True:
            try:
                temp = raw_input(">>> ").strip()
                spaces = temp.count(" ")
                print(spaces)
                if spaces == 1:
                    givenOption, name = temp.split()
                    print(givenOption, name )
                elif spaces == 2:
                    givenOption, name, number = temp.split()
                    print(givenOption, name, number)
                break
            except:
                print("asdasa")
