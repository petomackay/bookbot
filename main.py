def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()


def get_word_count(text):
    return len(text.split())


def get_char_counts(text):
    count_dict = {}
    for char in text:
        lowered_char = char.lower()
        count_dict[lowered_char] = count_dict.get(lowered_char, 0) + 1
    return count_dict


def get_sorted_char_counts(char_counts):
    sorted_char_counts = [{"char": char, "count": count} for char, count in char_counts.items()]
    sorted_char_counts.sort(key=sort_by_count, reverse=True)
    return sorted_char_counts


def sort_by_count(char_count_entry):
    return char_count_entry["count"]


def main():
    book_path = "books/frankenstein.txt"

    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    char_counts = get_char_counts(book_text)

    print(f"--- Begin report of {book_path} ---")

    print(f"{word_count} words found in the document")
    print()
    for char_count in get_sorted_char_counts(char_counts):
        if char_count["char"].isalpha():
            print(f"The '{char_count['char']}' character was found {char_count['count']} times")

    print("--- End report ---")


if __name__ == "__main__":
    main()
