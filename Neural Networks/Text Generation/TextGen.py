import keras
import numpy as np
import random

import io
path = keras.utils.get_file(
    'nietzsche.txt',
    origin='https://s3.amazonaws.com/text-datasets/nietzsche.txt')
with io.open(path, encoding='utf-8') as f:
    text = f.read().lower()

chars = sorted(list(set(text)))
char_indices = dict((c, i) for i, c in enumerate(chars))
indices_char = dict((i, c) for i, c in enumerate(chars))

sentences = []
next_chars = []
for i in range(0, len(text) - 40, 3):
    sentences.append(text[i: i + 40])
    next_chars.append(text[i + 40])

x = np.zeros((len(sentences), 40, len(chars)), dtype=np.bool)
y = np.zeros((len(sentences), len(chars)), dtype=np.bool)
for i, sentence in enumerate(sentences):
    for t, char in enumerate(sentence):
        x[i, t, char_indices[char]] = 1
    y[i, char_indices[next_chars[i]]] = 1
    
model = keras.models.Sequential()
model.add(keras.layers.LSTM(128, input_shape=(40, len(chars))))
model.add(keras.layers.Dense(len(chars), activation='softmax'))

optimizer = keras.optimizers.RMSprop(lr=0.01)
model.compile(loss='categorical_crossentropy', optimizer=optimizer)

def sample(preds, temperature=1.0):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)
  
model.fit(x, y, batch_size=18, epochs=1)

start_index = random.randint(0, len(text) - 40 - 1)
for diversity in [0.2, 0.5, 1.0, 1.2]:
    generated = ''
    sentence = text[start_index: start_index + 40]
    generated += sentence

    for i in range(400):
        x_pred = np.zeros((1, 40, len(chars)))
        for t, char in enumerate(sentence):
            x_pred[0, t, char_indices[char]] = 1.

        preds = model.predict(x_pred, verbose=0)[0]
        next_index = sample(preds, diversity)
        next_char = indices_char[next_index]

        generated += next_char
        sentence = sentence[1:] + next_char
        
with open('example.txt', 'w') as f:
    f.write(generated)
