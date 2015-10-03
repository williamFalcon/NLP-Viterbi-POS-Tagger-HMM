__author__ = 'waf04'
import nltk

def calculate_ngram_probabilities_for_corpus(corpus, n):
    """
    Returns an array of n dictionaries with the ngram probabilities for that ngram.
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
            zip_word_frequency_with_dict(sentence, ith_dict, ith_gram)

    print('yo')


def zip_word_frequency_with_dict(sentence, n_dict, n_count):
    """
    Inserts the frequency counts into the given dictionary
    :param sentence:
    :param n_dict:
    :param n_count:
    :return:
    """
    tokens = nltk.word_tokenize(sentence)

    # make ngram if have proper length
    if len(tokens) > 0:
        grammed = ngram_from_word_list(tokens, n_count)
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
