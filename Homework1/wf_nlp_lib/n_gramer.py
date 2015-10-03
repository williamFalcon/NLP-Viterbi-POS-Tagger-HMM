__author__ = 'waf04'
import math


def make_ngrams_for_corpus(corpus, n, start_token, end_token):
    """
    Returns an array of n dictionaries with the frequencies of each ngram
    :param corpus:
    :param n:
    :param start_token:
    :param end_token:
    :return:
    """
    # Ensure we have necessary params
    if not corpus or n == 0 or not start_token or not end_token: return [], 0

    # Init a dictionary for the ith ngram requested
    grams = [{} for i in range(n)]
    corpus_size = 0

    # Generate ith gram for each sentence given
    for i_gram_count in range(n):

        # Track current ngram place
        ith_gram = i_gram_count+1
        ith_dict = grams[i_gram_count]

        # Do frequency count
        for sentence in corpus:
            tokens = sentence.strip().split(' ')
            if len(tokens) > 0:
                corpus_size += len(tokens)+1 # Count the start token
                __insert_start_end_tokens(tokens, start_token, end_token)
                __zip_word_frequency_with_dict(tokens, ith_dict, ith_gram)

    # We counted corpus_size by a factor of n. Remove the factor for true count
    corpus_size /= n
    return grams, corpus_size


def calculate_ngram_probabilities(n_grams_array, corpus_size):
    """
    Calculates ngram propabilities of an array of dictionaries of sequential ngrams.
    :param n_grams_array:
    :param corpus_size:
    :return:
    """
    __internal_probabilitize(n_grams_array, len(n_grams_array)-1, corpus_size)


def __internal_probabilitize(dict_array, current_dict_index, corpus_size):

    # Current ngram dict
    gram_dict = dict_array[current_dict_index]

    # Base case. We're at the unigram. Normalize by vocab size
    if current_dict_index == 0:
        gram_dict.update((k, math.log(float(v) / float(corpus_size), 2)) for k, v in gram_dict.items())
        return

    # Recursive operations
    # Use the previous ngram as the numerator
    prior_gram_dict = dict_array[current_dict_index-1]

    # Calculate probability for each gram
    for gram in gram_dict:
        gram_dict[gram] = __log_probability_for_gram(gram, gram_dict, prior_gram_dict, 2)

    # Recurse
    __internal_probabilitize(dict_array, current_dict_index-1, corpus_size)


def __log_probability_for_gram(gram, gram_dict, prior_gram_dict, log_base):
    """
    Use the n-1 gram dict to calculate n-gram dict probability
    p = ngram / n-1GramDict(ngram[0:-1])
    :param gram:
    :param gram_dict:
    :param prior_gram_dict:
    :param log_base:
    :return:
    """
    prior_words = gram[0:-1]
    probability = float(gram_dict[gram]) / float(prior_gram_dict[prior_words])
    return math.log(probability, log_base)


def __insert_start_end_tokens(tokens, start_token, end_token):
    tokens.insert(0, start_token)
    tokens.append(end_token)


def __zip_word_frequency_with_dict(tokens, n_dict, n_count):
    """
    Inserts the frequency counts into the given dictionary
    :param tokens:
    :param n_dict:
    :param n_count:
    :return:
    """

    # make ngram
    grammed = __ngram_from_word_list(tokens, n_count)

    # freq count each ngram
    for gram in grammed:
        n_dict[gram] = n_dict[gram]+1 if gram in n_dict else 1


def __ngram_from_word_list(word_list, n):
    """
    Returns List of n-tuples from the given list
    :param word_list:
    :param n:
    :return:
    """
    return zip(*[word_list[i:] for i in range(n)])
