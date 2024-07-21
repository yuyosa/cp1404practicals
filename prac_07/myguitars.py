import csv
from guitar import Guitar

def main():
    filename = 'guitars.csv'
    guitars = load_guitars(filename)

    guitars.sort()
    print("\nGuitars by Year:")
    display_guitars(guitars)

    while True:
        name = input("Name：")
        if not name:
            break
        year = int(input("Year："))
        cost = float(input("Cose："))
        guitars.append(Guitar(name, year, cost))

    save_guitars(filename, guitars)

    print("\nNewest guitar list:")
    display_guitars(guitars)

def load_guitars(filename):
    guitars = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                name, year, cost = row
                guitars.append(Guitar(name, year, cost))
    return guitars


def display_guitars(guitars):
    for guitar in guitars:
        print(guitar)


def save_guitars(filename, guitars):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])





if __name__ == "__main__":
    main()
   