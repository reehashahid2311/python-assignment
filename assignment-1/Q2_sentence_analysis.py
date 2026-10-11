def analysis(sentence):
    words = sentence.split()

    if not words:
        print("Please enter a sentence with at least one word.")
        return

    unique = set(words)
    vowels = sum(char.lower() in "aeiou" for char in sentence)

    results = [
        "Total words: " + str(len(words)),
        "Total characters: " + str(len(sentence)),
        "Longest word: " + max(words, key=len),
        "Shortest word: " + min(words, key=len),
        "Vowels: " + str(vowels),
        "Unique words: " + str(unique),
        "Alphabetical order: " + str(sorted(unique))
    ]

    for item in results:
        print(item)

    with open("word_analysis.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(results))


analysis(input("Sentence: "))
