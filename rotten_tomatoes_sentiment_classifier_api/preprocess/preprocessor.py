from tensorflow.python.keras.preprocessing.text import Tokenizer
from tensorflow.python.keras.preprocessing.sequence import pad_sequences
import pickle
import os
from preprocess import package_constant


def texts_to_pad_seq(messages):
    tokenizer = pickle.load(
        open(os.path.join(package_constant.PREPROCESSOR_ROOT_DIR, "assets", "tokenizer.pickle"), "rb"))
    text_pad_sql = pad_sequences(tokenizer.texts_to_sequences(messages), maxlen=package_constant.MAX_SEQUENCE_LENGTH)

    return text_pad_sql
