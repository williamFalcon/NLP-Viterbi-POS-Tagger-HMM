__author__ = 'waf04'
import nltk


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
                zip_word_frequency_with_dict(sentence, ith_dict, ith_gram)

    return grams


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
        n_dict[gram] = n_dict[gram]+1 if gram in n_dict else 0


def ngram_from_word_list(word_list, n):
    """
    Returns List of n-tuples from the given list
    :param word_list:
    :param n:
    :return:
    """
    return zip(*[word_list[i:] for i in range(n)])
