__author__ = 'waf04'
import numpy.testing as numpy_tester
import logging


def test_grams(unigrams, bigrams, trigrams):
    """
    Tests QA1
    :param unigrams:
    :param bigrams:
    :param trigrams:
    :return:
    """
    print '==============================='
    print 'Part A1: Running ngram tests...'
    print '==============================='

    # Build tests
    uni_tests = [{("captain",): -14.2809819899}, {("captain's",): -17.0883369119}, {("captaincy",): -19.4102650068}]
    bi_tests = [{("and", "religion"): -12.9316608989}, {("and", "religious"): -11.3466983981}, {("and", "religiously"): -13.9316608989}]
    tri_tests = [{("and", "not", "a"): -4.02974734339}, {("and", "not", "by"): -4.61470984412}, {("and", "not", "come"): -5.61470984412}]

    # Assemble tests and grams to run tests easily
    all_tests = [uni_tests, bi_tests, tri_tests]
    n_grams = [unigrams, bigrams, trigrams]

    # Run all tests
    i = 1
    total_tests = 9
    for test, n_gram in zip(all_tests, n_grams):
        for uni_test in test:
            key, value = uni_test.popitem()
            val = n_gram[key]
            numpy_tester.assert_almost_equal(value, val)
            print '%i/%i Test passed (%s)' %(i, total_tests, key)
            i += 1


def test_score_grams(unigram_scores, bigram_scores, trigram_scores):
    """
    Tests QA2
    :param unigram_scores:
    :param bigram_scores:
    :param trigram_scores:
    :return:
    """
    print '==============================='
    print 'Part A2: Running scoring tests...'
    print '==============================='

    # Build tests
    uni_tests = [-178.726835483, -259.85864432, -143.33042989]
    bi_tests = [-92.1039984276, -132.096626407, -90.185910842]
    tri_tests = [-26.1800453413, -59.8531008074, -42.839244895]

    # Assemble tests and grams tto run tests easily
    all_tests = [uni_tests, bi_tests, tri_tests]
    ngrams_count = len(all_tests)
    n_grams = [unigram_scores[0:ngrams_count], bigram_scores[0:ngrams_count], trigram_scores[0:ngrams_count]]

    # Run all tests
    i = 1
    total_tests = 9
    for test, n_gram in zip(all_tests, n_grams):
        for idx, real in enumerate(test):
            answer = n_gram[idx]
            try:
                numpy_tester.assert_almost_equal(real, answer)
                print '%i/%i Test passed (%s)' %(i, total_tests, answer)
            except:
                logging.error('%i/%i Test failed DESIRED:(%s) != ACTUAL:(%s)' %(i, total_tests, real, answer))

            i += 1


def test_interpolation_scores(scores):
    """
    Tests QA3
    :param scores:
    :return:
    """
    print '==============================='
    print 'Part A3: Running interpolation tests...'
    print '==============================='

    # Assemble tests and grams tto run tests easily
    all_tests = [-46.5891638973, -85.77421559, -58.5442024163, -47.5165051948, -52.7387360815]

    # Run all tests
    i = 1
    total_tests = len(all_tests)
    for actual, desired in zip(all_tests, scores):
        try:
            numpy_tester.assert_almost_equal(actual, desired)
            print '%i/%i Test passed (%s)' %(i, total_tests, actual)
        except:
            logging.error('%i/%i Test failed DESIRED:(%s) != ACTUAL:(%s)' %(i, total_tests, actual, desired))

            i += 1