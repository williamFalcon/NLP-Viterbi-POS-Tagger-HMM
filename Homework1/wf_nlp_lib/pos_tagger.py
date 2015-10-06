__author__ = 'waf'
import wf_nlp_lib.smoother as smoother
import wf_nlp_lib.n_gramer as n_gramer
import math
import numpy

def tag(words_to_tag, possible_tags, known_words, trigram_probs, emission_probs, start_token='*', stop_token='STOP'):

    tagged = []

    # P(ADV | NOUN, NOUN)
    tags_transition_matrix = transition_probabilities_for_ngram_list(trigram_probs)

    # P(tag | word)
    possible_word_tags = transition_probabilities_for_ngram_list(emission_probs)

    for word_list in words_to_tag:
        n_gramer.insert_start_end_tokens(word_list, start_token, stop_token, 3)
        path = viverti_path(word_list, possible_tags, known_words, tags_transition_matrix, possible_word_tags)

    return 0


def viverti_path(word_list_observations, possible_tags_states, known_words, tags_transition_matrix, emissions_matrix):
    path = []

    # Where do I carry the info from the previous pass?
    for i in range(3, len(word_list_observations)):
        prior, current = grams_from_list_at_index(i, word_list_observations)
        possible_next_tags_from_prior = transitions_for_prior(prior, tags_transition_matrix) #something wrong here
        possible_next_tags_for_word = transitions_for_prior((current, ), emissions_matrix)
        possible_word_tags_likelihood = calculate_new_probabilities_for_state(possible_next_tags_for_word, possible_next_tags_from_prior)
        predicted_tag = arg_max_from_tag_list(possible_word_tags_likelihood)
        path.append(predicted_tag)
        print ''

    return []

def arg_max_from_tag_list(tags):

    max_val = 0
    tg = ''
    for k, v in tags.items():
        if v > max_val:
            v = max_val
            tg = k

    return tg


def calculate_new_probabilities_for_state(possible_next_tags, prior_key):
    result = {}
    for k, v in possible_next_tags.items():
        val = prior_key[k] if k in prior_key else -1000
        result[k] = v*val

    return result

def transition_probabilities_for_ngram_list(ngrams):
    """
    Returns tags transition matrix
    :param ngrams:
    :return:
    """
    matrix = {}
    for k, v in ngrams.items():
        prior = k[0:-1]
        current = k[-1]
        pairs_dict = matrix[prior] if prior in matrix else {}
        pairs_dict[current] = v
        matrix[prior] = pairs_dict

    return matrix


def grams_from_list_at_index(i, word_list):
    """
    Returns the trigram split up for this word sequence
    :param i:
    :param word_list:
    :return:
    """
    word_tri = tuple(word_list[i-3:i])
    prior = word_tri[0:-1]
    current = word_tri[-1]
    return prior, current


def transitions_for_prior(prior, tags_transitions):
    """
    Returns the possible transitions from this prior (bigram, etc...)
    Probabilities of going from this prior to the next tags
    :param prior:
    :param tags_transitions:
    :return:
    """
    transitions = tags_transitions[prior] if prior in tags_transitions else -1000
    return transitions


def possible_tags_for_word(input_word, tags):

    possible_tags = {}
    most_probable_tag = ''
    most_probable_tag_prob = float("-infinity")
    for k, v in tags.items():
        word, tg = k
        if word == input_word:
            possible_tags[tg] = v
            if v > most_probable_tag_prob:
                most_probable_tag = tg
                most_probable_tag_prob = v

    return possible_tags, most_probable_tag


def emission_probabilities_from(words, tags):
    """
    Calculates the log probability of seeing a tag given a word
    :param words:
    :param tags:
    :return: Emissions, known_tags
    """
    # Get frequency counts of tags (denominator)
    freqs = smoother.frequency_dict(tags)

    # Get (word, tag) freq count
    pair_freqs = pair_frequency(words, tags)

    # Calculate log probs
    emy = calculate_emissions(pair_freqs, freqs)

    known_tags = set(freqs.keys())
    return emy, known_tags


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

