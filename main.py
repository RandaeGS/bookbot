def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        print(word_cound(file_contents))
        print(character_count(file_contents))

def character_count(file):
    file = file.lower()
    characters = {}
    for ch in file:
        if ch in characters:
            characters[ch] += 1
        else:
            characters[ch] = 1

    return characters

def word_cound(file):
    return len(file.split())


main()
