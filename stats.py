def count_words(content):
    content_split = content.split()
    print(f"Found {len(content_split)} total words")

def count_char(content):
    char_count = {}
    new_content = content.lower()
    for char in new_content:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    print(char_count)