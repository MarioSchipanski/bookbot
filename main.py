import sys
from stats import words_count, character_count, dict_to_sorted_list

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:

    def get_book_text(filepath):
        with open(filepath) as f:
            return f.read()

    char_dict = character_count(get_book_text(sys.argv[1]))
    sorted_char_dict = dict_to_sorted_list(char_dict)

    def main():

        book_content = get_book_text(sys.argv[1])
        print("============ BOOKBOT ============")
        print("Analyzing book found at " + sys.argv[1] + "...")
        print("----------- Word Count ----------")
        print("Found " + str(words_count(book_content)) + " total words")
        print("-------- Character Count -------")
        for pair in sorted_char_dict:
            print(pair["char"] + ": " + str(pair["num"]))
        print("============= END ===============")

    main()