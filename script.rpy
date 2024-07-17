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
        $ floss = False
        $ lotion = False
        $ facewash = False
        $ snacks = False
        $ waterBottle = False

        image warmclothes:
            "warmclothes.png"
            zoom 0.5
        
        image lightclothes:
            "lightclothes.png"
            zoom 0.5

    
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
                show warmclothes at center with dissolve
                "You have packed 'warm clothes'."
                hide warmclothes
            "Light clothes":
                $ lightClothes = True
                show lightclothes at center with dissolve
                "You have packed 'light clothes'."
                hide lightclothes
            "Both":
                $ warmClothes = True
                show warmclothes at center with dissolve
                "You have packed 'warm clothes'."
                hide warmclothes
                $ lightClothes = True
                show lightclothes at center with dissolve
                "You have packed 'light clothes'."
                hide lightclothes
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
                "You have packed 'laptop'."
            "Charger":
                "You have packed 'charger'."
                $ charger = True
            "Plane ticket and passport":
                "You have packed 'plane ticket and passport'."
                $ ticketPassport = True
        jump bedroom

label kitchen:
    #scene kitchen COUGH COUGH WHO'S COLORING THIS

    "What do you look at?"

    menu:
        "Pantry":
            jump pantry
        "Cabinet":
            jump cabinet
        "Fridge":
            jump fridge
        "Leave the kitchen":
            jump main

    label pantry:
        "There are chips, chocolate, and other snacks that you like. What do you get?"
        menu: 
            "Chips":
                "You have packed 'chips'."
                $ snacks = True
            "Chocolate":
                "You have packed 'chocolate'."
                $ snacks = True
            "Other snacks":
                "You have packed 'other snacks'."
                $ snacks = True
        jump kitchen

    label cabinet:
        $ waterBottle = True
        "You grab a water bottle."
        jump kitchen

    label fridge:
        if waterBottle:
            "There's a water dispenser. You fill up your water bottle."
        else:
            "What are you doing here?"
            "(Hint: Get a water bottle.)"
        jump kitchen

label bathroom:
    scene bathroom:
        zoom 1.75

    "What do you look at?"

    menu:
        "Shower":
            "There's a towel and your shampoo and conditioner. What do you grab?"
            menu:
                "Towel":
                    "You have packed 'towel'."
                    $ towel = True
                "Shampoo and conditioner":
                    "You have packed 'shampoo and conditioner'."
                    $ shampooConditioner = True
            jump bathroom
        "Sink":
            "There's your toothbrush, toothpaste, and floss. What do you get?"
            menu:
                "Toothbrush":
                    "You have packed 'toothbrush'."
                    $ toothbrush = True
                "Toothpaste":
                    "You have packed 'toothpaste'."
                    $ toothpaste = True
                "Floss":
                    "You have packed 'floss'."
                    $ floss = True
            jump bathroom
        "Cabinet":
            "There's lotion and facewash. Which do you get?"
            menu:
                "Lotion":
                    "You have packed 'lotion'."
                    $ lotion = True
                "Facewash":
                    "You have packed 'facewash'."
                    $ facewash = True
            jump bathroom
        "Mirror":
            "Hey look, it's you!"
            jump bathroom
        "Leave the bathroom":
            jump main

label credits:
    "'Eduardo 'Edujante' Fornieles' on Behance.net\n'Yami-Yami' on ArtStation.com\n'Nadia Bykova' on Artpal.com\n'David Keen' on davidkeenart.com"
    "Prop art by Sky, Rachel, & Khloe\nCode by Abigail & Khloe"
    jump finish

label end:
    if canada == True:
        scene canada_bg:
            zoom 2.75
        "You made it to Canada!"
    elif newyork == True:
        scene newyork_bg:
            zoom 2.0
        "You made it to New York!"
    else:
        scene greece_bg:
            zoom 1.5
        "You made it to Greece!"

    "Thank you for playing. Enjoy your vacation!"
    jump finish

label finish:

    menu:
        "View credits":
            jump credits
        "End game":
            return


return
