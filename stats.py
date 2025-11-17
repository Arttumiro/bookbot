def get_book_words(filepath):
    with open(filepath) as f:
        num_words = f.read()
        num_words = num_words.split()
    return num_words

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_book_characters(filepath):
    with open(filepath) as f:
        counts = {}
        text = f.read().lower()
        for ch in text:
            if ch in counts:
                counts[ch] += 1
            else:
                counts[ch] = 1
    return counts


def sort_on(item):
    return item["num"]

def character_stats(char_dict):
    """
    Takes a dictionary of characters → counts
    and returns a list of dictionaries sorted by frequency (descending).

    Output format:
    [
        {"char": "a", "num": 1234},
        {"char": "b", "num": 567},
        ...
    ]
    """
    stats_list = []

    for char, count in char_dict.items():
        # Skip non-alphabetical characters
        if not char.isalpha():
            continue

        stats_list.append({"char": char, "num": count})

    # Sort greatest → least by "num"
    stats_list.sort(key=sort_on, reverse=True)

    return stats_list
