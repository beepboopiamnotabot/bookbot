
def get_word_count(string):
    return len(string.split())

def get_char_occurrences(string):
    char_counts = {}
    lowered_string = string.lower()
    for character in lowered_string:
        if character not in char_counts:
            char_counts[character] = 1
        else:
            char_counts[character] += 1
    
    return char_counts

def read_file(filepath):
    with open(filepath) as f:
        return f.read()

def create_list(dict):
    new_list = []
    for key in dict:
        if key.isalpha():
            new_list.append({"character" : key, "count" : dict[key]})
    return new_list



def main():
        filepath = "books/frankenstein.txt"
        file_contents = read_file(filepath)
        file_word_count = get_word_count(file_contents)
        file_character_occurrence = get_char_occurrences(file_contents)
        character_occurrence_list = create_list(file_character_occurrence)

        character_occurrence_list.sort(reverse=True, key=(lambda dict : dict["count"]))

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{file_word_count} words in the document\n")
        for char_count in character_occurrence_list:
            print(f"The '{char_count["character"]}' character was found {char_count["count"]} times")
        
        print("--- End report ---")
        

main()