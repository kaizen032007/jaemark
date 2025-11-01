def listing():
    foods_option = [
        "sinigang",
        "adobo",
        "caldareta",
        "dinuguan",
        "menudo",
        "paksiw",
    ]
    foods_option.sort()
    
    while True:
        print("-" * 40)
        print("   Hello welcome to the food selection!")
        print("   Choose an option on your liking!")
        print("-" * 40)
        print("")
        
        options = ["1. Show menu", "2. Exit", "3. Developer Options\n"]
        for option in options:
            print(option)

        user = input("Please choose an option: ")

        if user == "1":
            print("")
            for food in foods_option:
                print(food)
            user_option = input("\nChoose the food you want: ")

            if user_option in foods_option:
                print(f"Please pay 99 pesos for the {user_option}")
                payment = input("Are you using cash or cashless?: ")
                if payment == "cash":
                    print("The delivery driver will be there. Thank you for choosing us!\n")
                    back_option = input("Do you want to go back?: (yes/no): ")
                    if back_option == 'yes':
                        continue
                    elif back_option == 'no':
                        break
                    else:
                        print("Error: The system crashed")
                        break

                elif payment == "cashless":
                    print("The QR code will be presented to your messages. Thank you for choosing us!")
                    back_option1 = input("Do you want to go back?: (yes/no): ")
                    if back_option1 == 'yes':
                        continue
                    elif back_option1 == 'no':
                        break
                    else:
                        print("Error: The system crashed")
                        break

                else:
                    print("Invalid Payment please try again\n")

            else:
                print("-" * 40)
                print("Food doesn't exist please try again\n")

        elif user == "2":
            print("Thank you for visiting!")
            exit()

        elif user == "3":
            print("\nWelcome to developer options [RESTRICTED AREA DEVELOPER ONLY]\n")
            developer_options = [
                "1. Access the Foods",
                "2. Add Foods",
                "3. Remove Foods",
                "4. Checking item list\n",
            ]
            for developer in developer_options:
                print(developer)

            user_developer = input("Please choose what modification you will do: ")
            if user_developer == "1":
                print(f"This is the foods {foods_option}")

            elif user_developer == "2":
                print("To change the food please enter")
                new_food = input("Enter: ")
                foods_option.append(new_food)
                foods_option.sort()
                print(f"\nHere is the new foods {new_food} {foods_option}")
            
            elif user_developer == '3':
                pass

        else:
            print(f"'{user}' is not a valid option. Please try again.\n")


listing()
