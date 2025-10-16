from stats import count_words, get_char_count, sort_char_count, print_char_counts

def get_book_text(file):
    print("Analyzing book found at books/frankenstein.txt...")
    with open(file) as f:
        file_contents = f.read()
        # print(file_contents)
        print("----------- Word Count ----------")
        count_words(file_contents)
        print("--------- Character Count -------")
        char_count = get_char_count(file_contents)
        sorted_char_count = sort_char_count(char_count)
        print_char_counts(sorted_char_count)



def main():
    print("============ BOOKBOT ============")
    get_book_text("books/frankenstein.txt")
    print("============= END ===============")

main()
