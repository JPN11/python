import requests
from collections import Counter
import string

def count_words(text):
    # Remove punctuation from the text
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Split the text into words
    words = text.split()
    
    # Create an empty list to store the words
    word_list = []
    
    # Iterate through the words and add them to the list
    for word in words:
        word_list.append(word)
    
    # Return the list of words
    return word_list


def check_spelling(word, api_key):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    return response.status_code == 200

def analyze_text(text):
    words = count_words(text)
    word_count = len(words)
    word_freq = Counter(words)
    most_common_words = word_freq.most_common(10)

    misspelled_words = [word for word in words if not check_spelling(word, api_key)]

    print(f"Total number of words: {word_count}")
    print(f"Number of misspelled words: {len(misspelled_words)}")
    print("Most commonly used words:")
    for word, freq in most_common_words:
        print(f"{word}: {freq}")

    print("Misspelled words:")
    print(", ".join(misspelled_words))

# Replace 'your_api_key' with your actual API key if needed
api_key = 'your_api_key'

# Prompt the user for the file path
text = input("Enter text: ")
analyze_text(text)
