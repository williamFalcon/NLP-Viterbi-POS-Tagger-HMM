__author__ = 'waf'
import collections
import n_gramer


def replace_rare_words(corpus, known_words, rare_symbol):
    """
    Replaces rare words in corpus from known_words.
    :param corpus:
    :param known_words: List of whitelisted words
    :param rare_symbol: Symbol used in replacement
    """
    results = []

    # Iterate sentence
    for sentence in corpus:
        dirty_words = n_gramer.explode(sentence)
        clean_words = []

        # Replace word if rare
        for word in dirty_words:
            clean_words.append(word) if word in known_words else clean_words.append(rare_symbol)

        # Place back in corpus as word list
        results.append(clean_words)

    return results


def words_over_n_set(n, corpus):
    """
    Returns a set of words appearing over the n threshold
    :param n:
    :param corpus:
    :return:
    """
    results = set()

    # Get frequency counts
    freqs = frequency_dict(corpus)

    # Add words over threshold (not inclusive) to set
    for k, v in freqs.items():
        if v > n:
            results.add(k)

    return results


def frequency_dict(corpus):
    """
    Returns frequency counts for a corpus.
    :param corpus: Array of sentences (strings)
    :return:
    """
    all_words = {}

    for sentence in corpus:
        word_list = n_gramer.explode(sentence)
        for word in word_list:
            all_words[word] = all_words.get(word, 0) + 1

    return all_words
