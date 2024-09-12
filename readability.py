def count_letters(text):
    # Return the number of letters in text
    letters = 0
    for char in text:
        if char.isalpha():
            letters += 1
    return letters

def count_words(text):
    # Return the number of words in text
    words = text.split()
    return len(words)

def count_sentences(text):
    # Return the number of sentences in text
    sentences = 0
    for char in text:
        if char in ['.', '?', '!']:
            sentences += 1
    return sentences

def main():
    # Prompt the user for some text
    text = input("Text: ")

    # Count the number of letters, words, and sentences in the text
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    # Compute the Coleman-Liau index
    L = (letters / words) * 100
    S = (sentences / words) * 100
    index = 0.0588 * L - 0.296 * S - 15.8

    # Print the grade level
    grade = round(index)
    if grade < 1:
        print("Before Grade 1")
    elif grade > 16:
        print("Grade 16+")
    else:
        print(f"Grade {grade}")

if __name__ == "__main__":
    main()

