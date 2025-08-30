def get_num_words(book):
    words = book.split()
    return f"Found {len(words)} total words"


def count_characters(book):
    
    characters = {"a": 0, "b" : 0, "c" : 0, "d" : 0, 
                  "e": 0, "f" : 0, "g" : 0, "h" : 0, 
                  "i": 0, "j" : 0, "k" : 0, "l" : 0, 
                  "m": 0, "n" : 0, "o" : 0, "p" : 0, 
                  "q": 0, "r" : 0, "s" : 0, "t" : 0, 
                  "u": 0, "v" : 0, "w" : 0, "x" : 0, 
                  "y": 0, "z" : 0}
    words = book.lower()
    #    print(f"{len(book)} is our book length?")
    for i in range(0, len(words)):
        if words[i] in characters:
            characters[words[i]] += 1
    return sort_characters(characters)
    

'''
# python
def sort_on(item):
    return item["num"]

def sort_characters(counts):
    sorted_chars = []
    for ch in counts:
        sorted_chars.append({"char": ch, "num": counts[ch]})
    sorted_chars.sort(reverse=True, key=sort_on)
    print(sorted_chars)
'''


def sort_on(item):
    return item["num"]

def sort_characters(counts):
    sorted_chars = []
    for char in counts:
        sorted_chars.append({"char" : char, "num": counts[char]})
    #test
    #print(sorted_chars)
    # python
    #for i, it in enumerate(sorted_chars):
    #    if "num" not in it:
    #        print("Bad item at", i, it)
    #sorting
    sorted_chars.sort(reverse=True, key=sort_on)
    #test
    return sorted_chars




def sort_key(item):
    return item["age"]

def test_sort():
    my_dict = []
    my_dict = [{"name" : "Tabitha", "age": 11}, {"name": "Elizabeth", "age" : 49},
               {"name" : "Willie", "age": 47}, {"name" : "Biscuit", "age" : 7}]
    print(f"before sorting: {my_dict}")
    my_dict.sort(reverse=True, key=sort_key)
    print(my_dict)