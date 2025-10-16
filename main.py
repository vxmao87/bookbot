import sys
from stats import count_words, get_char_count, sort_char_count, print_char_counts

def get_book_text(file):
    print(f"Analyzing book found at {file}...")
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
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    get_book_text(sys.argv[1])
    print("============= END ===============")

main()
