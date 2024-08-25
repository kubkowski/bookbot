def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    return len(text.split())

def characters_count(text):
    characters_count = {}
    lowered_text = text.lower()
    for character in lowered_text:
        if character in characters_count:
            characters_count[character] += 1
        else:
            characters_count[character] = 1

    return characters_count

def sort_on(dict):
    return dict["count"]

def convert_dictionary_to_sorted_list(dictionary):
    list_of_characters = []
    for character in dictionary:
        if character.isalpha():
            list_of_characters.append({"character": character, "count": dictionary[character]})
    list_of_characters.sort(reverse=True, key=sort_on)    
    return list_of_characters

def main():
    path = "books/frankenstein.txt"
    book_text = get_book_text(path)
    number_of_words = word_count(book_text)
    dictionary_of_characters = characters_count(book_text)
    list_of_characters = convert_dictionary_to_sorted_list(dictionary_of_characters)
    print(f'--- Begin report of {path} ---')
    print(f'{number_of_words} words found in the document')
    for character in list_of_characters:
        print(f"The '{character['character']}' character was found {character['count']} times")
    print("--- End report ---")

main()
