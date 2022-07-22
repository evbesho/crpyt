
while True:
    print("Welcome to Tony's Message decoder!")
    print("\n1. Encode a Message")
    print("2. Decode a Message")
    print("3. Exit")

    try:
        choice = int(input("\nPlease enter which menu item you would like to choose: "))
    except ValueError:
        print("\n *INVALID CHOICE* Please enter a number on the menu. \n")
        continue

# code for encrypting message
    if choice == 1:
        en_key = input("\nPlease enter integer encryption key value: ")

        try:
            int(en_key)
        except ValueError:
            print("\n *INVALID ENCRYPTION KEY* Back to main menu. \n")
            continue

        es_in = input("\nEnter message to be encrypted: ")

        es_return = ""
        index = 0
        for char in es_in:
            acs = ord(char) + int(en_key[index])
            es_return += chr(acs)
            index += 1

            if index == len(en_key): index = 0

        print("\nEncrypted message: ")
        print("\t " + es_return + "\n")

# code for decrypting message
    elif choice == 2:
        de_key = input("\nPlease enter decryption key: ")

        try:
            int(de_key)
        except ValueError:
            print("\n *INVALID ENCRYPTION KEY* Back to main menu. \n")
            continue

        ds_in = input("\nEnter message to be decrypted: ")

        ds_return = ""
        index = 0
        for char in ds_in:
            acs = ord(char) - int(de_key[index])
            ds_return += chr(acs)
            index += 1

            if index == len(de_key): index = 0

        print("\nDecrypted message: ")
        print("\t " + ds_return + "\n")

# ending loop if exit is selected
    elif choice == 3:
        print("\nThank you for using my message decoder! Come again!")
        break

# for ints outside of scope of the menu
    else:
        print("\n *INVALID CHOICE* Please enter a number on the menu. \n")