def count_words(content):
    content_split = content.split()
    print(f"Found {len(content_split)} total words")


def get_char_count(content):
    char_count = {}
    new_content = content.lower()
    for char in new_content:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count


def sort_on(items):
    return items["num"]


def sort_char_count(char_dict):
    final_dict = []
    for char in char_dict:
        temp_dict = {}
        if char.isalpha():
            temp_dict["char"] = char
            temp_dict["num"] = char_dict[char]
            final_dict.append(temp_dict)
    
    final_dict.sort(reverse=True, key=sort_on)
    return final_dict


def print_char_counts(dict_list):
    for dict in dict_list:
        print(f"{dict["char"]}: {dict["num"]}")

