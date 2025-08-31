def number_of_words(book):
    wordlist = str.split(book)

    return len(wordlist)

def num_of_chars(book):
    book_lower = book.lower()

    character_list = {}
    
    for char in book_lower:
        if char in character_list:
            character_list[char] += 1
        else:
            character_list[char] = 1

    return character_list

def sort_dict(dict):
    return sorted(dict.items(), key=lambda item: item[1], reverse=True )
    