student = {"name":"Ritik","marks": [70,66,79]}

def get_index_key_value():
    print("Do you want to Enter Key or Index :- ")
    print("1. Key ")
    print("2. Index")
    print("3. Exit")
    try :
        choice = int(input("Enter your choice : "))
    except ValueError:
        print("!! Invalid Choice !! Enter a valid Choice")
    if choice == 1:
        try :
            key = input("Enter a Key : ")
            print(student[key])
        except KeyError:
            try:
                print(student[int(key)])
                print("Key dosen't Exist Check the key value you Entered!!")
            except KeyError:
                print("Key dosen't Exist Check the key value you Entered!!")
    elif choice == 2:
        try :
            index = int(input("Enter a Index value : "))
            print(student["marks"[index]])
        except ValueError:
            print("Invalid Index Value")
        except IndexError:
            print("Index does not exist")
    elif choice == 3:
        print("Thanks for your time")
        return 
    else :
        print("Enter a Valid Choice")
        get_index_key_value()

get_index_key_value()