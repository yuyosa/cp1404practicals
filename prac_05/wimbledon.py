def main():
    filename = "wimbledon.csv"
    data = read_file(filename)
    champions = process_champions(data)
    countries = process_countries(data)
    print("Wimbledon Champions:")
    for champion, wins in sorted(champions.items()):
        print(f"{champion} {wins}")

    print("\nThese {} countries have won Wimbledon:".format(len(countries)))
    print(", ".join(countries))


def read_file(filename):
    with open(filename, "r",encoding="utf-8-sig") as in_file:
        data = []
        for line in in_file:
            data.append(line.strip().split(','))
    return data

def process_champions(data):
    champions = {}
    for row in data:
        name = row[2]
        if name in champions:
            champions[name] += 1
        else:
            champions[name] = 1
    return champions


def process_countries(data):
    countries = set()
    for row in data:
        country = row[1]
        countries.add(country)
    return sorted(countries)



main()