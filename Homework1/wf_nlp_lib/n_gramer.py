__author__ = 'waf04'
import nltk
import math


def make_ngrams_for_corpus(corpus, n, start_token, end_token):
    """
    Returns an array of n dictionaries with the frequencies of each ngram
    :param corpus:
    :param n:
    :return:
    """

    # Init a dictionary for the ith ngram requested
    grams = [{} for i in range(n)]

    # Generate ith gram for each sentence given
    for i_gram_count in range(n):

        # Track current ngram place
        ith_gram = i_gram_count+1
        ith_dict = grams[i_gram_count]

        # Do frequency count
        for sentence in corpus:
            tokens = nltk.word_tokenize(sentence)
            if len(tokens) > 0:
                insert_start_end_tokens(tokens, start_token, end_token)
                zip_word_frequency_with_dict(tokens, ith_dict, ith_gram)

    return grams


def probabilitize_n_grams(n_grams_array):
    internal_probabilitize(n_grams_array, len(n_grams_array)-1)


def internal_probabilitize(dict_array, current_dict_index):

    # Base case. We're at the unigram
    if current_dict_index == 0:
        return

    # Use the previous ngram as the numerator
    gram_dict = dict_array[current_dict_index]
    prior_gram_dict = dict_array[current_dict_index-1]

    # Calculate probability for each gram
    for gram in gram_dict:
        gram_dict[gram] = log_probability_for_gram(gram,gram_dict, prior_gram_dict, 2)

    # Recurse
    internal_probabilitize(dict_array, current_dict_index-1)


def log_probability_for_gram(gram, gram_dict, prior_gram_dict, log_base):
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


def insert_start_end_tokens(tokens, start_token, end_token):
    tokens.insert(0, start_token)
    tokens.append(end_token)


def zip_word_frequency_with_dict(tokens, n_dict, n_count):
    """
    Inserts the frequency counts into the given dictionary
    :param tokens:
    :param n_dict:
    :param n_count:
    :return:
    """

    # make ngram
    grammed = ngram_from_word_list(tokens, n_count)

    # freq count each ngram
    for gram in grammed:
        n_dict[gram] = n_dict[gram]+1 if gram in n_dict else 1


def ngram_from_word_list(word_list, n):
    """
    Returns List of n-tuples from the given list
    :param word_list:
    :param n:
    :return:
    """
    return zip(*[word_list[i:] for i in range(n)])
