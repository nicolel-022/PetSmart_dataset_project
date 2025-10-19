# HELPER FUNCTIONS

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('petsmart_store_data.csv')
# Remove empty values
df.dropna(inplace = True)

# Dict mapping Category to Url Keyword
names_to_brands = {
    
    'cat': '/cat/',
    'dog': '/dog/',
    'fish': '/fish/',
    'bird': '/bird/',
    'reptile': '/reptile/',
    'small pet': '/small-pet/'
    }

brands = ['/cat/', '/dog/', '/fish/', '/bird/', '/reptile/', '/small-pet/']
names = ['cat', 'dog', 'fish', 'bird', 'reptile', 'small pet']

# HELPER FUNCTIONS
def USD_to_CAD(price):
    return round(price * 1.36, 2)


def clean_numbers():
    '''
    (None) -> None

    Corrects the data type of certain values

    '''
    
    # Clean numbers
    df['price'] = df['price'].str.replace(',', '').astype(float)
    
    # Convert to CAD
    df['price'] = df['price'].apply(USD_to_CAD)
    
    return None

def get_brands(category):
    category = names_to_brands[category]
    brands = df.loc[df['url'].str.contains(category, regex=False, na=False), 'brand'].unique()
    return brands

    
# MAIN FUNCTIONS

def show_overview():
    '''
    (None) -> str

    Shows the number of brands per category
    Shows the number of products per catgeory
    Shows the average rating of brands for each category
    (<2 : Very Negative)
    (2<3 : Negative)
    (3<4 : Fair)
    (4<=5 : Very Good)
    '''
    
    # Print the number of brands for each category
    for i in range(0, len(brands), 1):
        
        unique = get_brands(names[i])
        num_unique_brands = len(unique)
        print("There are " + str(num_unique_brands) + " brands that sell " + names[i] + " products")

    #Print number of products per category
    for i in range(0, len(brands), 1):
        
        products = df.loc[(df['url'].str.contains(brands[i], regex=False, na=False)) & (df.availability == 'InStock'), 'name'].unique()
        count = len(products)
        print("There are " + str(count) + " " + names[i] + " available products")

    #Find the average rating of products per catgeory
    for i in range(0, len(brands), 1):

        avgRating = df.loc[ df['url'].str.contains(brands[i], regex=False, na=False), 'avg_rating'].mean()
        quality = ''
        
        if (avgRating < 2):
            quality = 'Very Negative'
        elif (avgRating > 2 and avgRating < 3):
            quality = 'Slightly Negative'
        elif (avgRating > 3 and avgRating < 4):
            quality = 'Positive'
        elif (avgRating > 4 and avgRating <= 5):
            quality = 'Very Positive'
            
        print("Average Rating of " + names[i] + " products: " + str(round(avgRating, 1)) + " (" + quality + ")")
             
    return None


def compare_by_price(category):
    '''
    (String) -> None

    Produces a graph displaying the average price of every brand under a specific category

    '''
    
    # Get the average price of every brand for a specific category
    category_name = names_to_brands[category]
    brands = get_brands(category)
    x = np.array(brands)
    y = []
    
    for i in range(0, len(brands), 1):
        brand_products = df.loc[(df['url'].str.contains(category_name, regex=False, na=False)) & (df.brand == brands[i]), 'price']
        avg_price = brand_products.median()
        y.append(avg_price)
        print("The average cost of a " + brands[i] + " product is $" + str(round(avg_price, 2)))

    # Generate bar graph with the average prices
    plt.bar(x,y)
    plt.title("Average Product Cost of Brands")
    plt.xlabel("Brand Names")
    plt.ylabel("Price in CAD")
    plt.show()
    
    return None


def compare_by_rating(category):
    '''
    (String) -> None

    Produces a graph displaying the average rating of every brand under a specific category

    '''

    # Get average rating
    category_name = names_to_brands[category]
    brands = get_brands(category)
    x = np.array(brands)
    y = []

    for i in range(0, len(brands), 1):
        brand_ratings = df.loc[(df['url'].str.contains(category_name, regex=False, na=False)) & (df.brand == brands[i]), 'avg_rating']
        avg_rating = brand_ratings.mean()
        y.append(avg_rating)
        print("The average rating for a " + brands[i] + " product is " + str(round(avg_rating, 1)))
                               
    # Generate bar graph with the average prices
    plt.bar(x,y)
    plt.title("Average Ratings for Brands")
    plt.xlabel("Brand Names")
    plt.ylabel("Rating")
    plt.show()
    
    return None

def find_best_products(category, min_price, max_price, min_rating):
    # Get URL keyword
    category_name = names_to_brands[category]
    get_products = df.loc[(df['url'].str.contains(category_name, regex=False, na=False)) & (df.price >= min_price) & (df.price <= max_price) & (df.avg_rating >= min_rating), 'name']
    product_List = get_products.unique()
    if (len(brands) != 0):
        print("Check out these products: ", product_List)
    else:
        print("No products were found. Try changing your preferences")
        
    return None
