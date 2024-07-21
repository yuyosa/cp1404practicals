"""
pseudocode:
Set Dictionary

while true:
    get choice

    if choice == "":
        print goodbye
        break
    if choice not in set_color_list
        print error

    else:
        print(choice, choice_code)
"""

set_color_list = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "Apricot": "#fbceb1", "Alizarin crimson": "#e32636",
                  "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc", "Aqua": "#00ffff", "Aquamarine1": "#ffefdb",
                  "Aquamarine2": "#7fffd4"}


while True:
    choice = input("Please enter the color you want to choose (or press Enter to exit): ").title()

    if choice == "":
        print("Goodbye!")
        break
    elif choice not in set_color_list:
        print("Error, please select a color name that exists.")
    else:
        print(f"The color code for {choice} is {set_color_list[choice]}")


"""
Word Occurrences
Estimate: 20 minutes
Actual:   18 minutes
"""