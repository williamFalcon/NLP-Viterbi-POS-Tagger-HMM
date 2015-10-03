__author__ = 'waf04'
import pickle


def save_ngrams(ngrams, filename):
    pickle.dump(ngrams, open(filename, "wb"))


def load_ngrams(filename):
    if file_accessible(filename, 'r'):
        data = pickle.load(filename)
        return data

    return


def file_accessible(filepath, mode):
    try:
        f = open(filepath, mode)
        f.close()
    except IOError as e:
        return False

    return True