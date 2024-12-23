def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        print(word_cound(file_contents))

def word_cound(file):
    return len(file.split())


main()
