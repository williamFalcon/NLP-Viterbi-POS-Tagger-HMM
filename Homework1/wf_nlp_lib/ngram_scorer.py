__author__ = 'waf04'
import n_gramer as gramer


def score(ngram_p, n, corpus, start_token, end_token):
    results = []
    for sentence in corpus:

        # Create ntuples from sentence
        word_list = __build_word_list(sentence, start_token, end_token, n)
        n_tuple = gramer.ngram_from_word_list(word_list, n)

        total = 0

        for sentence_tuple in n_tuple:
            total += ngram_p[sentence_tuple]

        results.append(total)

    return results


def interpolate_ngram_collection(ngram_collection, corpus, start_token, end_token):

    # n is how big our ngram is
    n = len(ngram_collection)
    lambds = lambdas_from_ngrams(ngram_collection)

    results = []
    for sentence in corpus:

        # Create ntuples from sentence
        word_list = __build_word_list(sentence, start_token, end_token, n-1)
        n_tuple = gramer.ngram_from_word_list(word_list, n)

        total = 0

        for sentence_tuple in n_tuple:
            powerset = powerset_from_collection(sentence_tuple)
            subtotal = 0
            for idx, sub_tuple in enumerate(powerset):
                lmbd = lambds[idx]
                value = ngram_collection[idx][sub_tuple]
                subtotal += lmbd*value

            total += subtotal

        results.append(total)

    return results

def powerset_from_collection(maxtuple):
    """
    Generates all the subsets of the input (without the empty set)
    Example: (a, b, c) = [a, (a,b), (a,b,c)]
    :param maxtuple:
    :return:
    """

    length = len(maxtuple)
    results = []
    for i in range(length):
        results.append(maxtuple[i:])

    # Reverse the result
    return results[::-1]


def lambdas_from_ngrams(ngrams):
    result = []
    n_size = len(ngrams)
    [result.append(float(1.0)/n_size) for ngram in ngrams]
    return result


def __build_word_list(sentence, start_token, end_token, n):
    word_list = gramer.explode(sentence)
    gramer.insert_start_end_tokens(word_list, start_token, end_token, n)

    return word_list