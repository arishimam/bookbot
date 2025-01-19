def count_words(text)->int:
    words = len(text.split()) 

    return words

def count_chars(text)->dict:
    char_counts = {}
    for c in text:
        char = c.lower() 
        char_counts[char] = char_counts.get(char, 0) + 1

    return char_counts

def main():
    file_path = "books/frankenstein.txt"
    with open(file_path) as f:
        file_contents = f.read()
    word_count = count_words(file_contents)
    char_dict = count_chars(file_contents)

    print(f"---Begin report of {file_path} ---")
    print(f"{word_count} words found in the document")
    print()

    for k in char_dict:
        if k == ' ' or k == '#' or k == '.':
            continue
        print(f"The '{k}' character was found {char_dict[k]} times")


    print("--- End report ---")

if __name__== "__main__":
    main()
