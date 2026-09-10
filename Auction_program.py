import random
auction_items = [
    # Fine Art & Sculptures
    "18th-Century Oil Painting 'Sunset over Venice'",
    "Original Hand-Signed Picasso Sketch (1942)",
    "Contemporary Abstract Marble Sculpture by Kenji",
    "Renaissance-Era Bronze Bust of a Nobleman",

    # Luxury & Historical Jewelry
    "24-Carat Flawless Blue Diamond Necklace",
    "Imperial Emerald Brooch from the Romanov Dynasty",
    "Vintage 1950s Patek Philippe Perpetual Calendar Watch",
    "Ancient Roman Gold Signet Ring (2nd Century)",

    # Rare Collectibles & Artifacts
    "First Edition Copy of 'The Great Gatsby' (Signed)",
    "Authentic Lunar Meteorite Fragment (120g)",
    "17th-Century Japanese Samurai Katana with Scabbard",
    "Handwritten Lyrics to a Classic Beatles Song",

    # Luxury Vehicles & Yachts
    "Restored 1963 Aston Martin DB5 (Silver Birch)",
    "Limited-Edition Concept Hypercar (1 of 5)",
    "Vintage 1920s Indian Twin-Cylinder Motorcycle",

    # Fine Wine & Rare Instruments
    "Bottle of 1945 Domaine de la Romanée-Conti Wine",
    "1715 Stradivarius Violin 'The Angel'",
    "Grand Steinway Concert Piano (Macassar Ebony)",

    # High-End Real Estate & Experiences
    "Private Island Parcel in the French Polynesia",
    "Vintage Louis Vuitton Steamer Trunk (Circa 1910)"
]
product=random.choice(auction_items)
print(product)
auction_scene = f"""
                 [ THE PRESTIGE AUCTION HOUSE ]
  
     MALE AUCTIONEER                            FEMALE CO-LEAD
  "We open the bidding                      "Verifying current online bids"
   for {product}\n"                            
  
                    
        (o  o)                                        (•  •)
         _\\==/_                                      _\\--/_
        /  __  \\                                   /  __  \\
       / /|  |\\ \\                                 / /|  |\\ \\
      / / |  | \\ \\                               / / |  | \\ \\
     / /  |  |  \\ \\                             / /  |  |  \\ \\
    (_/   |  |   \\_)                           (_/    |  |   \\_)
         /____\\                                       /____\\
                                           
                                                                             
                                           
        [______]                                   [______]
           ||                                         ||
           ||                                         ||
  _________||_________                       _________||_________
 /                    \\                     /                    \\

|                      |                   |                      |
|______________________|                   |______________________|
        ||    ||                                   ||    ||
        ||    ||                                   ||    ||
  ======''====''======                       ======''====''======
  
                     _______________________

                    |                       |
                    |   .----------------.  |
                    |  |   ||||||||||||   | |
                    |  |   ||| ART ||||   | | <-- The Auction Object
                    |  |   ||||||||||||   | |     {product}
                    |   '----------------'  |
                    ------------------------
"""
print(auction_scene)
Auction_stats={}
Auction_over=True
while (Auction_over != False):
    auction_input=input("is there any other user if so enter yes or no:")
    if auction_input=="yes":
        name=input("what is your name: ")
        price=int(input("what is your bidding amount:$ "))
        auctioner_unique_id=input("what is your assigned unique auctioner id: ")
        Auction_stats[auctioner_unique_id] = [name, price]
        max_item = max(Auction_stats.items(),key=lambda item: item[1][1])
    elif auction_input=="no":
        Auction_over=False
        print(f"{max_item} is the winner of this set")
    else:
        print("just choose between yes and no actually")
        Auction_over=False





