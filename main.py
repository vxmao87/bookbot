from stats import count_words, count_char

def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
        print(file_contents)
        count_words(file_contents)
        count_char(file_contents)


def main():
    get_book_text("books/frankenstein.txt")

main()
