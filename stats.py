from typing import Dict, List

def get_word_count(text: str):
    return len(text.split())

def get_char_frequency(text: str):
    char_frequency: Dict[str, int] = {}

    for c in text:
        c = c.lower()
        if char_frequency.__contains__(c):
            char_frequency[c] += 1
        else:
            char_frequency[c] = 1

    return char_frequency

def sort_on(dictionary):
    return dictionary['count']

def get_alpha_sorted(frequencies):
    sorted_list = []
    for f in frequencies:
        if f.isalpha():
            sorted_list.append({"char" : f, "count" : frequencies[f]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
