# Points per letter
POINTS = [
    1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4,
    10
]


def compute_score(word):
    # Keep track of score
    score = 0

    # Compute score for each character
    for char in word:
        if char.isupper():
            score += POINTS[ord(char) - ord('A')]
        elif char.islower():
            score += POINTS[ord(char) - ord('a')]

    return score


def main():
    # Prompt the players for two words
    word1 = input("Player 1: ")
    word2 = input("Player 2: ")

    # Calculate the score of each word
    score1 = compute_score(word1)
    score2 = compute_score(word2)

    # Determine and print the winner
    if score1 > score2:
        print("Player 1 wins!")
    elif score1 < score2:
        print("Player 2 wins!")
    else:
        print("Tie!")


if __name__ == "__main__":
    main()
