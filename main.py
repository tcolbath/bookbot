def main():
    with open("books/frankenstein.txt") as f:
        book = f.read()
    title = f.name
    report(title, book) 

def count_words(book):
    words = book.split()
    return len(words)

def count_letters(book):
    text = book.lower()
    chars = {}

    for char in text:
        if char.isalpha():
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
    
    sort_keys = list(chars.keys())
    sort_keys.sort()
    sorted_chars = {i: chars[i] for i in sort_keys}

    return sorted_chars

def report(title, book):
    print(f"-- Report of {title} --\n\n There were", count_words(book), "words found in the document.\n")
    letters = count_letters(book)

    for letter in letters:
        print(f"'{letter.upper()}' was found", letters[letter], "times")

    print("\n -- End of report. --")
    
if __name__ == "__main__":
    main()