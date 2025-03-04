from stats import get_word_count, get_char_frequency, get_alpha_sorted
import sys

def get_book_text(path: str):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    book_text = get_book_text(sys.argv[1])
    num_words = get_word_count(book_text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    chars = get_alpha_sorted(get_char_frequency(book_text))
    for item in chars:
        print(f"{item['char']}: {item['count']}")

    print("============= END ===============")


main()
