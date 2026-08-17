"""
                                                                                                                                                    by. Tanish Tiwari
ATM MANAGEMENT SYSTEM
Professional Version
"""

""""""""""""

current_amount = 150000
saving_amount = 50000
pin = 2401

print("=" * 45)
print("        WELCOME TO ATM MANAGEMENT")
print("=" * 45)

while True:
    print("\nPlease Insert Your Card")
    lang = int(input("\n1. English\n2. Hindi\n3. Exit\n\nEnter Choice: "))

    match lang:
        case 3:
            print("\nThank you for using our ATM. Visit Again!")
            break

        case 1:
            acc = int(input("\n1. Saving Account\n2. Current Account\n\nEnter Choice: "))

            match acc:
                case 1:
                    while True:
                        print("\n------ SAVING ACCOUNT ------")
                        ch = int(input(
                            "1. Withdraw\n"
                            "2. Deposit\n"
                            "3. Check Balance\n"
                            "4. Back\n\n"
                            "Enter Choice: "
                        ))

                        match ch:
                            case 1:
                                amt = int(input("Enter withdrawal amount: "))
                                pi = int(input("Enter PIN: "))
                                if pi == pin:
                                    if amt <= 10000 and amt <= saving_amount:
                                        saving_amount -= amt
                                        print("Withdrawal Successful.")
                                        print("Remaining Balance:", saving_amount)
                                    elif amt > saving_amount:
                                        print("Insufficient Balance.")
                                    else:
                                        print("Daily withdrawal limit is ₹10000.")
                                else:
                                    print("Wrong PIN.")

                            case 2:
                                amt = int(input("Enter deposit amount: "))
                                pi = int(input("Enter PIN: "))
                                if pi == pin:
                                    saving_amount += amt
                                    print("Deposit Successful.")
                                    print("Updated Balance:", saving_amount)
                                else:
                                    print("Wrong PIN.")

                            case 3:
                                pi = int(input("Enter PIN: "))
                                if pi == pin:
                                    print("Available Balance:", saving_amount)
                                else:
                                    print("Wrong PIN.")

                            case 4:
                                break

                            case _:
                                print("Invalid Choice.")

                case 2:
                    while True:
                        print("\n------ CURRENT ACCOUNT ------")
                        ch = int(input(
                            "1. Withdraw\n"
                            "2. Deposit\n"
                            "3. Check Balance\n"
                            "4. Back\n\n"
                            "Enter Choice: "
                        ))

                        match ch:
                            case 1:
                                amt = int(input("Enter withdrawal amount: "))
                                pi = int(input("Enter PIN: "))
                                if pi == pin:
                                    if amt <= 25000 and amt <= current_amount:
                                        current_amount -= amt
                                        print("Withdrawal Successful.")
                                        print("Remaining Balance:", current_amount)
                                    elif amt > current_amount:
                                        print("Insufficient Balance.")
                                    else:
                                        print("Daily withdrawal limit is ₹25000.")
                                else:
                                    print("Wrong PIN.")

                            case 2:
                                amt = int(input("Enter deposit amount: "))
                                pi = int(input("Enter PIN: "))
                                if pi == pin:
                                    current_amount += amt
                                    print("Deposit Successful.")
                                    print("Updated Balance:", current_amount)
                                else:
                                    print("Wrong PIN.")

                            case 3:
                                pi = int(input("Enter PIN: "))
                                if pi == pin:
                                    print("Available Balance:", current_amount)
                                else:
                                    print("Wrong PIN.")

                            case 4:
                                break

                            case _:
                                print("Invalid Choice.")

                case _:
                    print("Invalid Account Type.")

        case 2:
            acc = int(input("\n1. सेविंग अकाउंट\n2. करंट अकाउंट\n\nअपना विकल्प चुनें: "))

            match acc:
                case 1:
                    while True:
                        print("\n------ सेविंग अकाउंट ------")
                        ch = int(input(
                            "1. निकासी\n"
                            "2. जमा\n"
                            "3. बैलेंस देखें\n"
                            "4. वापस जाएँ\n\n"
                            "अपना विकल्प चुनें: "
                        ))

                        match ch:
                            case 1:
                                amt = int(input("निकासी राशि दर्ज करें: "))
                                pi = int(input("पिन दर्ज करें: "))
                                if pi == pin:
                                    if amt <= 10000 and amt <= saving_amount:
                                        saving_amount -= amt
                                        print("निकासी सफल।")
                                        print("शेष बैलेंस:", saving_amount)
                                    elif amt > saving_amount:
                                        print("पर्याप्त बैलेंस नहीं है।")
                                    else:
                                        print("दैनिक निकासी सीमा ₹10000 है।")
                                else:
                                    print("गलत पिन।")

                            case 2:
                                amt = int(input("जमा राशि दर्ज करें: "))
                                pi = int(input("पिन दर्ज करें: "))
                                if pi == pin:
                                    saving_amount += amt
                                    print("जमा सफल।")
                                    print("अपडेटेड बैलेंस:", saving_amount)
                                else:
                                    print("गलत पिन।")

                            case 3:
                                pi = int(input("पिन दर्ज करें: "))
                                if pi == pin:
                                    print("उपलब्ध बैलेंस:", saving_amount)
                                else:
                                    print("गलत पिन।")

                            case 4:
                                break

                            case _:
                                print("अमान्य विकल्प।")

                case 2:
                    while True:
                        print("\n------ करंट अकाउंट ------")
                        ch = int(input(
                            "1. निकासी\n"
                            "2. जमा\n"
                            "3. बैलेंस देखें\n"
                            "4. वापस जाएँ\n\n"
                            "अपना विकल्प चुनें: "
                        ))

                        match ch:
                            case 1:
                                amt = int(input("निकासी राशि दर्ज करें: "))
                                pi = int(input("पिन दर्ज करें: "))
                                if pi == pin:
                                    if amt <= 25000 and amt <= current_amount:
                                        current_amount -= amt
                                        print("निकासी सफल।")
                                        print("शेष बैलेंस:", current_amount)
                                    elif amt > current_amount:
                                        print("पर्याप्त बैलेंस नहीं है।")
                                    else:
                                        print("दैनिक निकासी सीमा ₹25000 है।")
                                else:
                                    print("गलत पिन।")

                            case 2:
                                amt = int(input("जमा राशि दर्ज करें: "))
                                pi = int(input("पिन दर्ज करें: "))
                                if pi == pin:
                                    current_amount += amt
                                    print("जमा सफल।")
                                    print("अपडेटेड बैलेंस:", current_amount)
                                else:
                                    print("गलत पिन।")

                            case 3:
                                pi = int(input("पिन दर्ज करें: "))
                                if pi == pin:
                                    print("उपलब्ध बैलेंस:", current_amount)
                                else:
                                    print("गलत पिन।")

                            case 4:
                                break

                            case _:
                                print("अमान्य विकल्प।")

                case _:
                    print("गलत विकल्प।")

        case _:
            print("Please enter a valid option.")
