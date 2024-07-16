# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#define e = Character("Eileen")

define p = Character("[playerName]")

# The game starts here.

label start:

    python:
        playerName = renpy.input("Enter your name: ")
        playerName.strip()
        
    p "Final exams are finally over."
    p "I've wanted to travel to somewhere for so long, and now I finally have time to go."
    p "Let's see, I want to go to..."

    $ canada = False
    $ greece = False
    $ newyork = False

    menu:
        "Canada":
            $ canada = True
            $ location = "Canada"
        "Greece":
            $ greece = True
            $ location = "Greece"
        "New York":
            $ newyork = True
            $ location = "New York"

    if canada == True:
        p "Let's go to Canada!"
        "(Hint: Pack warmer clothing.)"
    elif greece == True:
        p "Let's go to Greece!"
        "(Hint: Pack lighter clothing.)"
    else:
        p "Let's go to New York!"
        "(Hint: Pack both warm and light clothing.)"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    p "So now that I've decided where to go, I need to pack appropriately."
    
    label main:

        scene hall:
            zoom 1.5

        $ warmClothes = False
        $ lightClothes = False
        $ laptop = False
        $ charger = False
        $ ticketPassport = False
        $ towel = False
        $ shampooConditioner = False
        $ toothbrush = False
        $ toothpaste = False
        $ lotion = False
        $ facewash = False
        $ snacks = False
        $ waterBottle = False

    
        p "Where should I look?"

        menu:
            "Bedroom":
                "You enter the bedroom." 
                jump bedroom
            "Kitchen":
                "You enter the kitchen."
                jump kitchen
            "Bathroom":
                "You enter the bathroom."
                jump bathroom
            "I've finished packing":
                jump end

label bedroom:
    scene bedroom:
        zoom 1.3

    "What do you look at?"

    menu:
        "Closet":
            jump closet
        "Bed":
            jump bed
        "Desk":
            jump desk
        "Leave the bedroom":
            jump main

    label closet:
        "There's a pile of warm clothes and light clothes."
        "What do you pack?"

        menu:
            "Warm clothes":
                $ warmClothes = True
                "You have packed 'warm clothes'."
            "Light clothes":
                $ lightClothes = True
                "You have packed 'light clothes'."
            "Both":
                $ warmClothes = True
                $ lightClothes = True
                "You have packed 'warm clothes' and 'light clothes'."
                
        jump bedroom

    label bed:
        "It's just a bed."

        menu:
            "Examine further":
                "It's really just a bed. What are you, daydreaming? Go look at something else."
            "Go back":
                pass
        jump bedroom

    label desk:
        "There's your laptop, the charger, and your plane ticket and passport."
        "What do you pack?"

        menu:
            "Laptop":
                $ laptop = True
            "Charger":
                $ charger = True
            "Plane ticket and passport":
                $ ticketPassport = True
        
        jump bedroom

label kitchen:


label bathroom:


label end:

    if canada == True:
        scene canada_bg
        "You made it to Canada!"
    elif newyork == True:
        scene newyork_bg
        "You made it to New York!"
    else greece == True:
        scene greece_bg
        "You made it to Greece!"

    "Thank you for playing. Enjoy your vacation!"

    menu:
        "View art credits."
            jump artcredits
        "End game."
            return

label artcredits:

    "'Eduardo "Edujante" Fornieles' on Behance.net \n
