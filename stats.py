def count_words(text)->int:
    words = len(text.split()) 
    return words

def count_chars(text)->dict:
    char_counts = {}
    for c in text:
        char = c.lower() 
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

def sort_dict(dictionary)->dict:
    sorted_dict = dict(sorted(dictionary.items()))
    return sorted_dict
