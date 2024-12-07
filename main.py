import csv
import random
import xml.etree.ElementTree as ET

INPUT_FILE = "books-en.csv"
OUTPUT_FILE = "bibliography.txt"

books = []
with open(INPUT_FILE, newline='', encoding='cp1251') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        books.append(row)

# print(*books, sep='\n')

long_titles_count = sum(1 for book in books if 'Book-Title' in book and len(book['Book-Title']) > 30)
print(f"Количество записей с названием длиннее 30 символов: {long_titles_count}\n")

def search_books_by_author(author):
    results = [book for book in books if 'Book-Author' in book and author.lower() in book['Book-Author'].lower()]
    if results:
        print(f"Книги автора {author}:")
        for book in results:
            print(f"{book['Book-Author']} - {book['Book-Title']} ({book['Year-Of-Publication']})")
    else:
        print(f"Книг автора {author} не найдено.")

author_to_search = input("Введите имя автора для поиска: ")
search_books_by_author(author_to_search)

random_books = random.sample(books, min(20, len(books)))
bibliography = [
    f"{i + 1}. {book['Book-Author']}. {book['Book-Title']} - {book['Year-Of-Publication']}"
    for i, book in enumerate(random_books)
]

with open(OUTPUT_FILE, 'w', encoding='cp1251') as f:
    f.write("\n".join(bibliography))

print(f"Библиографические ссылки сохранены в файл {OUTPUT_FILE}.")

tree = ET.parse('currency.xml')
root = tree.getroot()

char_codes = []
values = []
for currency in root.findall('Valute'):
    char_code = currency.find('CharCode').text
    value = float(currency.find('Value').text.replace(',', '.'))
    char_codes.append(char_code)
    values.append(value)

print()
print("CharCode:", char_codes)
print("Value:", values)