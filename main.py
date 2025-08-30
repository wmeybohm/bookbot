from stats import *
import sys


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents



def main():
    print("Usage: python3 main.py <path_to_book>")
    if len(sys.argv) < 2:
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    
    test_output = get_book_text(book_path)
    #(test_output)
    #Sprint("testing word count")
    word_count = get_num_words(test_output)
    char_output = count_characters(test_output)
    print(word_count)   
    #print(char_output) 
# python
    for item in char_output:
        ch = item["char"]
        if ch.isalpha():
           print(f"{ch}: {item['num']}")

main()
