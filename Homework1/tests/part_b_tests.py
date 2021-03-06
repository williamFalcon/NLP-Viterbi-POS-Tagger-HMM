__author__ = 'waf04'
import numpy.testing as numpy_tester
import logging


def test_trigrams_b2(trigrams):
    """
    Tests QB2
    :param trigrams:
    :return:
    """
    print '==============================='
    print 'Part B2: Running ngram tests...'
    print '==============================='

    # Build tests
    tri_tests = [{("*", "*", "ADJ"): -5.20557515082},
                 {("ADJ", ".", "X"): -9.99612036303},
                 {("NOUN", "DET", "NOUN"): -1.26452710647},
                 {("X", ".", "STOP"): -1.92922692559}
                 ]

    # Assemble tests and grams to run tests easily
    all_tests = [tri_tests]
    n_grams = [trigrams]

    # Run all tests
    i = 1
    total_tests = len(tri_tests)
    for test, n_gram in zip(all_tests, n_grams):
        for uni_test in test:
            key, value = uni_test.popitem()
            val = n_gram[key]
            numpy_tester.assert_almost_equal(value, val)
            print '%i/%i Test passed (%s)' %(i, total_tests, key)
            i += 1


def test_emissions(emissions):
    """
    Tests QB4
    :param emissions:
    :return:
    """
    print '==============================='
    print 'Part B4: Running ngram tests...'
    print '==============================='

    # Build tests
    tri_tests = [{("America", "NOUN"): -10.99925955},
                 {("Columbia", "NOUN"): -13.5599745045},
                 {("New", "ADJ"): -8.18848005226},
                 {("York", "NOUN"): -10.711977598}
                 ]

    # Assemble tests and grams to run tests easily
    all_tests = [tri_tests]

    # Run all tests
    i = 1
    total_tests = len(tri_tests)
    for test in tri_tests:
        key, value = test.popitem()
        val = emissions[key]
        numpy_tester.assert_almost_equal(value, val)
        print '%i/%i Test passed (%s)' %(i, total_tests, key)
        i += 1