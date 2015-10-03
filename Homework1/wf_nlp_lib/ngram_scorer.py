__author__ = 'waf04'
import n_gramer as gramer


def score(ngram_p, n, corpus, start_token, end_token):
    results = []
    for sentence in corpus:
        word_list = gramer.explode(sentence)
        insert_start_end_tokens(word_list, start_token, end_token, n)
        # Remove start token for unigrams
        if n == 1: word_list.pop(0)

        n_tuple = gramer.ngram_from_word_list(word_list, n)

        total = 0

        for sentence_tuple in n_tuple:
            total += ngram_p[sentence_tuple]

        results.append(total)

    return results

def insert_start_end_tokens(tokens, start_token, end_token, n_gram_count):

    for c in range(n_gram_count):
        tokens.insert(0, start_token)
        tokens.append(end_token)