def count_words(text):
    words_array = text.split()
    print(f"Found {len(words_array)} total words")
    return words_array

def count_chars(text):
    chars = {}
    for char in text:
        if char.lower() in chars:
            chars[f"{char.lower()}"] += 1
        else:
            chars[f"{char.lower()}"] = 1
    return chars

def sort_on(dict):
    return(dict["count"])

def report(counts):
    dicts = []
    for letter in counts:
        dict = {}
        count = counts[letter]
        dict["character"] = letter
        dict["count"] = count
        dicts.append(dict)
    dicts.sort(reverse=True, key=sort_on)
    return dicts
    # print(dicts)