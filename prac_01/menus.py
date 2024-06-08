"""Pseudocode:
Set menu
Get name
Get choice

while choice != Q
    print menu
    Get choice

    if choice == H
        print hello,name
    elif choice == G
        print goodbye,name
    elif choice == Q
        print finished
    else
        print Invalid choice
"""
menu = "(H)ello\n(G)oodbye\n(Q)uit"
name = input("Enter name: ")
choice = input("").upper()

while choice != "Q":
    print(menu)
    choice = input(" ").upper()

    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    elif choice == "Q":
        print("Finished.")
    else:
        print("Invalid choice")




