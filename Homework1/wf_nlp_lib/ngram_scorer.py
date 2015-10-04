__author__ = 'waf04'
import n_gramer as gramer
import math
import numpy as np

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
        word_list = __build_word_list(sentence, start_token, end_token, n)
        n_tuple = gramer.ngram_from_word_list(word_list, n)

        total = 0

        # print sentence
        for sentence_tuple in n_tuple:
            # print '======================='
            # print "%s" %(sentence_tuple,)
            powerset = powerset_from_collection(sentence_tuple)

            try:
                # Get log probabilities for this tuple across all ngrams
                log_probs = [item[powerset[i]] for i, item in enumerate(ngram_collection)]

                # Calculate log probability
                probs_sum = [2**log_prob for log_prob in log_probs]
                trigram_interpolated_log_prob = math.log(lambds[0], 2) + math.log(np.sum(probs_sum), 2)

                # Add to overall sentence count
                total += trigram_interpolated_log_prob
                # print '%f TOTAL:%f' %(trigram_interpolated_log_prob, total)
            except:
                # print 'skipped %s' %(sentence_tuple,)
                pass

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