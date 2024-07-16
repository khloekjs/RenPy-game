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

    p "test"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    #e "You've created a new Ren'Py game."

    #e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
