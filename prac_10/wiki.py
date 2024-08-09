import wikipedia

def main():
    info = input("Enter page title:")
    while info:
        result = get_wikipedia_summary(info)
        print(f"\n{result}\n")
        info = input("Enter page title:")
    print("Thank you")

def get_wikipedia_summary(info):
    try:
        page = wikipedia.page(info, auto_suggest=False)
        summary = page.summary
        return f"{page.title}\n{summary}\n{page.url}"

    except wikipedia.exceptions.PageError:
        return f'Page id "{info}" does not match any pages. Try another id!'

    except wikipedia.exceptions.DisambiguationError as i:
        return f'We need a more specific title. Try one of the following, or a new search:\n{i.options}'

    except Exception as i:
        return f"An error occurred: {i}"


main()


