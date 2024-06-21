"""
pseudocode:
main function
    set email_book

    while True:
        Get email
        if email == ""
            break

        name = extract_name_from_email()
        make sure name_ifo

        if name_ifo not in ['y', 'yes', '']:
            Get name

        email_book[email] = name

    for email, name in email_book.items():
        print(name  email")

extract_name_from_email()   function
    username = email.split('@')[0]
    parts = username.split('.')
    name = ' '.join(parts).title()
    return name

"""

def main():
    email_book = {}

    while True:
        email = input("Please enter your email:")
        if email == "":
            break

        name = extract_name_from_email(email)
        get_name = input(f"Is your name {name}? (y/n)").strip().lower()

        if get_name not in ['y', 'yes', '']:
            name = input("Please enter your name:")

        email_book[email] = name

    for email, name in email_book.items():
        print(f"{name} ({email})")


def extract_name_from_email(email):
    username = email.split('@')[0]
    parts = username.split('.')
    name = ' '.join(parts).title()
    return name


main()
