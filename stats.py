def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def count_words(book):
    return len(book.split())

def count_characters(book):
    char_counts = {}
    book = book.lower()
    for c in book:
        if c.isalpha():
            if c in char_counts:
                char_counts[c] += 1
            else:
                char_counts[c] = 1
    return char_counts

def sort_characters(char_counts):
    char_list = [{"char": char, "num": count} for char, count in char_counts.items()]
    char_list.sort(reverse=True, key=lambda x: x["num"])
    return char_list