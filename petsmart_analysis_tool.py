### PETSMART PRODUCT ANALYSIS TOOL ###

# Dataset downloaded from Kaggle

import petsmart_tools as ps

ps.clean_numbers()

intro_str = '''

Welcome to the PETSMART PRODUCT ANALYSIS TOOL!

MENU OPTIONS:

Note: Out of stock items are automatically excluded.

1 - Quick Overview: Shows number of brands per category, and average cost per category
2 - Compare brands by price per category
3 - Compare brands by rating per category
4 - Find a personalized product: Based on price range and desired rating
5 - Exit

'''

print(intro_str)
option = ""

# MENU
while (option != "5"):
    option = input("Enter an option: ")

    if (option == "1"):
        # Call fucntion show_overview
        ps.show_overview()


    elif (option == "2"):
        while True:
            # Ask the user to enter a Pet category
            cat_str = '''

            Dog       Cat
            Fish      Bird
            Reptile   Small Pet


            '''
            print(cat_str)
            cat = input("Please choose a category: ")
            cat = cat.lower()

            # If the input is invalid, asks again
            if (cat == "dog" or cat == "cat" or cat == "fish" or cat == "bird" or cat == "reptile" or cat == "small pet"):
                break
            else:
                print("Invalid input: Please try again")
                continue

        # Call the function compare_by_price
        ps.compare_by_price(cat)


    elif (option == "3"):
        while True:
            # Ask the user to enter a Pet category
            cat_str = '''

            Dog       Cat
            Fish      Bird
            Reptile   Small Pet


            '''
            print(cat_str)
            cat = input("Please choose a category: ")
            cat = cat.lower()

            # If the input is invalid, asks again
            if (cat == "dog" or cat == "cat" or cat == "fish" or cat == "bird" or cat == "reptile" or cat == "small pet"):
                break
            else:
                print("Invalid input: Please try again")
                continue
        ps.compare_by_rating(cat)


    elif (option == "4"):
        min_price = 0
        max_price = 0
        min_rating = 0

        while True:
            # Ask the user to enter a Pet category
            cat_str = '''

            Dog       Cat
            Fish      Bird
            Reptile   Small Pet


            '''
            print(cat_str)
            cat = input("Please choose a category: ")
            cat = cat.lower()

            # If the input is invalid, asks again
            if (cat == "dog" or cat == "cat" or cat == "fish" or cat == "bird" or cat == "reptile" or cat == "small pet"):
                break
            else:
                print("Invalid input: Please try again.")
                continue

        while True:
            # Ask the user to enter a min price
            min_price = float(input("Please enter a minimum price (Whole numbers only): "))

            # Handle invalid input
            if (min_price >= 0):
                break
            else:
                print("Invalid input: Please try again.")
                continue

        while True:
            # Ask the user to enter a max price
            max_price = float(input("Please enter a maxiumum price (Whole numbers only): "))

            # Handle invalid input
            if (max_price > min_price):
                break
            elif (max_price <= min_price):
                print("Error: Please choose a number greater than your minumum price.")
                continue
            else:
                print("Invalid input: Please try again.")
                continue

        while True:
            #Ask the user to enter a minimum rating
            min_rating = float(input("Please enter a minimum rating (1-5): "))
            
            if (min_rating > 1 and min_rating < 5):
                break
            else:
                print("Invalid input: Please try again.")
                continue

        # Call function find_best_products
        ps.find_best_products(cat, min_price, max_price, min_rating)

