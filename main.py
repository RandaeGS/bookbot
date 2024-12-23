def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        character_dict = character_count(file_contents)
        words = word_count(file_contents)
        print_report(words, character_dict)

def print_report(word_count, character_dict):

    sorted_dict = sorted(character_dict.items(), key=lambda x:x[1], reverse=True)

    print("--- Begin of report ---")
    print(f"{word_count} words found in the document")

    for key, value in sorted_dict:
        print(f"The {key} character was found {value} times")

    print("--- End of report ---")


def character_count(file):
    file = file.lower()
    characters = {}
    for ch in file:
        if ch in characters:
            characters[ch] += 1
        elif ch not in characters and ch.isalpha():
            characters[ch] = 1

    return characters

def word_count(file):
    return len(file.split())


main()
