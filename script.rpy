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

    #$ canada = False
    #$ greece = False
    #$ newyork = False

    menu:
        "Canada":
            $ canada = True
        "Greece":
            $ greece = True
        "New York":
            $ newyork = True

    if canada == True:
        p "Let's go to Canada!"
        p "(Hint: Pack warmer clothing.)"
    elif greece == True:
        p "Let's go to Greece!"
        p "(Hint: Pack lighter clothing.)"
    else:
        p "Let's go to New York!"
        p "(Hint: Pack both warm and light clothing.)"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene hall:
        zoom 1.5

    p "So now that I've decided where to go, I need to pack appropriately."

#---MAIN-------------------------

    label main:

        $ warmClothes = False
        $ lightClothes = False
        $ laptop = False
        $ charger = False
        $ planeTicket = False
        $ passport = False
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
                jump bedroom
            "Kitchen":
                jump kitchen
            "Bathroom":
                jump bathroom
            "I've finished packing.":
                jump end

#---BEDROOM-------------------------

label bedroom:
    "You enter the bedroom." 
    "What do you look at?"

    menu:
        "Closet":
            jump closet
        "Bed":
            jump bed
        "Desk":
            jump desk
        "Leave the bedroom.":
            jump main

    label closet:
        p "There's a pile of warm clothes and light clothes."
        p "What do you pack?"

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

    label bed:

    label desk:

#---KITCHEN-------------------------

label kitchen:


#---BATHROOM-------------------------

label bathroom:

#---SUITCASE-------------------------

label suitcase:

    "This is your suitcase."

#---END-------------------------

label end:

    if canada == True:
        "You made it to Canada!"
    
    return
