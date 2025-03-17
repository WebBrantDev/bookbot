from stats import count_words, count_chars, report
import sys

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return(file_contents)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    # print(get_book_text(book))
    # count_words(get_book_text(book))
    # count_chars(get_book_text(book))
    dicts = report(count_chars(get_book_text(sys.argv[1])))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    count_words(get_book_text(sys.argv[1]))
    print("--------- Character Count -------")
    for i in dicts:
        if i["character"].isalpha():
            print(f"{i["character"]}: {i["count"]}")
    print("============= END ===============")
main()
