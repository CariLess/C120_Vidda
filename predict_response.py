# Bibliotecas de preprocesamiento de datos de texto
import nltk

import json
import pickle
import numpy as np
import random

ignore_words = ['?', '!',',','.', "'s", "'m"]

# Cargar la biblioteca para el modelo
import tensorflow
from data_preprocessing import get_stem_words


model = tensorflow.keras.models.load_model('./chatbot_model.h5')

# Cargar los archivos de datos
intents = json.loads(open('./intents.json').read())
words = pickle.load(open('./words.pkl','rb'))
classes = pickle.load(open('./classes.pkl','rb'))

def preprocess_user_input(user_input):


def bot_class_prediction(user_input):


def bot_response(user_input):


while True:
    user_input = input("Type your message here:")
    print("User Input: ", user_input)

    response = bot_response(user_input)
    print("Bot Response: ", response)