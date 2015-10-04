__author__ = 'waf'
import n_gramer


def split_wordtags(corpus, delimiter='/', start_word='*', stop_word='STOP', ngram_used=3):
    """
    Splits a corpus into a words vector and a tag vector
    :param corpus:
    :param delimiter:
    :param start_word:
    :param stop_word:
    :param ngram_used: Default=3 . # of ngrams to use. Will insert start and stop accordingly.
    :return:
    """
    tag_sentences = []
    word_sentences = []

    # for each sentence
    for sentence in corpus:
        # split on space
        word_list = n_gramer.explode(sentence)
        words = []
        tags = []
        for el in word_list:
            word, tag = el.rsplit(delimiter, 1)
            words.append(word)
            tags.append(tag)

        # Insert start and end token in each vector
        n_gramer.insert_start_end_tokens(words, start_word, stop_word, ngram_used)
        n_gramer.insert_start_end_tokens(tags, start_word, stop_word, ngram_used)

        tag_sentences.append(words)
        word_sentences.append(tags)

    return word_sentences, tag_sentences
