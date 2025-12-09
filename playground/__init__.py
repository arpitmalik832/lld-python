import re


def word_frequencies(sentences: list[str]) -> dict[str, int]:
    # TODO:Flatten the list and join all sentences into a single string
    flattened_sentences = " ".join(sentences).lower()
    # TODO: Tokenization: Split the string into individual words
    words = re.findall(r"\w+", flattened_sentences)
    # TODO: Word Counting: Count the frequency of each word
    freq: dict[str, int] = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1

    # TODO: Return the dictionary of the words and frequencies
    return freq
