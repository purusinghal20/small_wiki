import wikipedia
import random

def wiki_data():
    search = input("search: ")
    result = wikipedia.page(search)
    print(result.title)
    print(result.content)

if __name__ == '__main__':
    wiki_data()
