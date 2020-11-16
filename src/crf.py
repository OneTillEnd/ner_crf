from sklearn_crfsuite import CRF

def word2feature(sentence, index):
    features = {
        'w': word,
        'w-1': prev_word,
        'w+1': next_word,
        'w-1:w': prev_word + word,
        'w:w+1': word + next_word
    }
