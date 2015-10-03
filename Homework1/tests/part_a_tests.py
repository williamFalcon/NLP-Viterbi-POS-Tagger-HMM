__author__ = 'waf04'
import numpy.testing as numpy_tester


def test_grams(unigrams, bigrams, trigrams):

    print 'Running ngram tests...'

    # Build tests
    uni_tests = [{("captain",): -14.2809819899}, {("captain's",): -17.0883369119}, {("captaincy",): -19.4102650068}]
    bi_tests = [{("and", "religion"): -12.9316608989}, {("and", "religious"): -11.3466983981}, {("and", "religiously"): -13.9316608989}]
    tri_tests = [{("and", "not", "a"): -4.02974734339}, {("and", "not", "by"): -4.61470984412}, {("and", "not", "come"): -5.61470984412}]

    # Assemble tests and grams tto run tests easily
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