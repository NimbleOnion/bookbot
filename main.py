import sys

def get_book_text (filepath):
    with open(filepath) as file:
        read_file = file.read()
    return read_file

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    from stats import word_count, character_count, sorted
    book_path = sys.argv[1]
    out = get_book_text(book_path)
    total_words = word_count(out)
    chr_count = character_count(out)
    sorted_list = sorted(chr_count)
    print_report(book_path, total_words, sorted_list)

def print_report(book_path, total_words, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()