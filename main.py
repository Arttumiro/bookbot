import sys
from stats import get_book_words, get_book_characters, character_stats

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    
    # ---------- WORD COUNT ----------
    print("----------- Word Count ----------")
    words = get_book_words(path)
    print(f"Found {len(words)} total words")
    
    # ---------- CHARACTER COUNT ----------
    print("--------- Character Count -------")
    char_dict = get_book_characters(path)
    sorted_characters = character_stats(char_dict)

    for item in sorted_characters:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()

