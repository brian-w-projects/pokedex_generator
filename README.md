# Pokedex Generator

### This program uses a neural network trained on all the available Pokedex entries to create new, fake Pokedex entries.

<img align='right' src='https://upload.wikimedia.org/wikipedia/en/9/92/Pok%C3%A9mon_episode_1_screenshot.png'/>

To use this program run the above file with one or two seed words. The seed words will act as the beginning of the entry. The words must have appeared at least once in a past Pokedex entry. 

You may also include an optional flag -t with a float from 0.1 to 1. The larger the number the more volatile the generated entries. Larger values may result in gibberish while smaller values may result in entries that are near copies of existing Pokedex entries. Default is 0.5

## Example Entries

* It has been found in amber. It is said to be the personification of the sea.
* It has a functional purpose. It releases the leaves on it's head. It shines brightly in the seven colors of the sea.
* This pokemon is known to fight and make a weary body feel invigorated.
* This pokemon is a significant ingredient in remedies for misdeeds 500 years ago.
* Never never stop bouncing! If it stops moving its body is covered by nonflammable fur. It can fly at speeds of roughly 29 knots quickly closing in on it's back.
* A Pokemon that has a body of a volcano, it flies at speeds of 75 mph by squirming and twisting its 10 tentacles.
* A single word: heartless.

<pre>
usage: pokedex_generator.py [-h] [-t TEMPERATURE] seed

Generate Pokedex entries by supplying seed word/words

positional arguments:
  seed            One or two words to seed Pokedex entry. EG: this pokemon

optional arguments:
  -h, --help      show this help message and exit
  -t TEMPERATURE  Float from 0.1 to 1. The higher this value the weirder the
                  entries. The lower the value, the more similar. Default: 0.5
</pre>
