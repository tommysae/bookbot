import sys

from stats import number_of_words
from stats import num_of_chars
from stats import sort_dict


def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    
    return file_contents


def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book = sys.argv[1]


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    print("----------- Word Count -----------")
    words = number_of_words(get_book_text(book))
    print(f"Found {words} total words") 

    print("--------- Character Count -------")
    characters = num_of_chars(get_book_text("books/frankenstein.txt"))
    sort_dict(characters)

    for letter, count in characters.items():
        print(f"{letter}: {count}")
    
if __name__ == "__main__":
    main()