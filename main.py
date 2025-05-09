from stats import count_words, count_chars, sort_dict
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    with open(file_path) as f:
        file_contents = f.read()
    word_count = count_words(file_contents)
    char_dict = count_chars(file_contents)
    sorted_char_dict = sort_dict(char_dict)

    print(f"---Begin report of {file_path} ---")
    print(f"Found {word_count} total words")
    print()

    for k,v in sorted_char_dict.items():
        if not k.isalpha():
            continue
        if k == ' ' or k == '#' or k == '.':
            continue
        print(f"{k}: {v}")


    print("--- End report ---")

if __name__== "__main__":
    main()
