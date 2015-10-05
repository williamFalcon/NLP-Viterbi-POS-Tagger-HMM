__author__ = 'waf'
import wf_nlp_lib.smoother as smoother
import wf_nlp_lib.n_gramer as n_gramer
import math


def emission_probabilities_from(words, tags):
    """
    Calculates the log probability of seeing a tag given a word
    :param words:
    :param tags:
    :return:
    """
    # Get frequency counts of tags (denominator)
    freqs = smoother.frequency_dict(tags)

    # Get (word, tag) freq count
    pair_freqs = pair_frequency(words, tags)

    # Calculate log probs
    emy = calculate_emissions(pair_freqs, freqs)

    return emy


def calculate_emissions(start_end_tuple_list, end_state_count_list, log_base=2):
    """
    Calculates log probabilites for each state transition
    :param start_end_tuple_list:
    :param end_state_count_list:
    :param log_base:
    :return:
    """
    emissions = {}

    # Calculate the emissions
    for pair in start_end_tuple_list:
        word, tag = pair
        emission_probability = float(start_end_tuple_list[pair]) / float(end_state_count_list[tag])

        # use log probability
        emissions[pair] = math.log(emission_probability, log_base)

    return emissions


def pair_frequency(list_a, list_b):
    """
    Frequency of a tuple from list_a and list_b
    :param list_a:
    :param list_b:
    :return: Dict with tuple as key, frequency count as value
    """
    tuple_freq = {}

    # Calculate frequencies for word, tag pair
    for word_list, tag_sentence in zip(list_a, list_b):
        tag_list = n_gramer.explode(tag_sentence)
        for word, tag in zip(word_list, tag_list):
            w_t_tuple = (word, tag)
            tuple_freq[w_t_tuple] = tuple_freq.get(w_t_tuple, 0) + 1

    return tuple_freq