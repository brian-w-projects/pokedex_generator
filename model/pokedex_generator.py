import pickle
from keras.models import load_model
import numpy as np
import argparse
import warnings


def reweight_distribution(original_distribution, temperature=0.5):
    """
    Re-weights the output distribution from the neural network based on the temperature value. The higher the
    temperature, the more even the distribution is. Created by Francois Chollet

    :param original_distribution: Predictions from neural network for possible subsequent words.
    :param temperature: Float from 0.1 to 1 representing the amount of redistribution of the prediction space.
    :return: Predictions from the neural network rescaled by the temperature value.
    """

    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        distribution = np.log(original_distribution) / temperature
        distribution = np.exp(distribution)
        return distribution / np.sum(distribution)


def create(seed, model, tokenizer, temp=0.5):
    """
    Runs seed text through the neural network repeatedly to create a fake Pokedex entry.

    :param seed: Two word list representing the seed text for the entry
    :param model: Neural network for generating Pokedex entries
    :param tokenizer: Dictionary of Pokedex entry words
    :param temp: Float from 0.1 to 1 representing the volatility of the generated entries
    :return: String representing the Pokedex entry
    """

    dictionary = [""] + list(tokenizer.index_word.values())
    start = np.array(tokenizer.texts_to_sequences(seed)).reshape(1, -1)
    if seed[0] == '<start>':
        output = [seed[-1]]
    else:
        output = seed[:]

    for _ in range(45):
        weights = reweight_distribution(model.predict(start), temperature=temp)
        word = np.random.choice(dictionary, size=1, p=weights[0, :])[0]
        if word == '<end>': 
            if len(output) > 10:
                break
            else:
                continue
        output.append(word)
        start = np.append(start[0, 1:], tokenizer.texts_to_sequences([word])).reshape(1, -1)
    return " ".join(output)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate Pokedex entries by supplying seed word/words')
    parser.add_argument('seed', action='store', help='One or two words to seed Pokedex entry. EG: this pokemon')
    parser.add_argument('-t', action='store', dest='temperature', help='Float from 0.1 to 1. The higher this value the\
     weirder the entries. The lower the value, the more similar. Default: 0.5')
    
    results = parser.parse_args()
    
    with open('tokenizer.pickle', 'rb') as p:
        tokenizer = pickle.load(p)
    
    seed = results.seed.lower().split(" ")
    try:
        tokenizer.texts_to_sequences(seed)
    except:
        print('Your seed word/words are not present in any Pokedex entry. Please use a seed that has appeared in\ '
              'a Pokedex entry.')
        raise SystemExit

    if len(seed) == 1:
        seed.insert(0, "<start>")

    model = load_model('model.h5')

    for i, _ in enumerate(range(10)):
        print(str(i) + ": " + create(seed, model, tokenizer, results.temperature or 0.5))
