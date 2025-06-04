import sys
from stats import get_book_text, count_words, count_characters, sort_characters

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    
    try:
        book = get_book_text(book_path)
        num_words = count_words(book)
        
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        
        char_counts = count_characters(book)
        sorted_chars = sort_characters(char_counts)
        
        print("--------- Character Count -------")
        for item in sorted_chars:
            print(f"{item['char']}: {item['num']}")
            
    except FileNotFoundError:
        print(f"Error: File not found at {book_path}")
        sys.exit(1)
    
    print("============= END ===============")

if __name__ == "__main__":
    main()

