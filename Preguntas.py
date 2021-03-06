__author__ = 'jpradas'
# -*- coding: utf-8 -*-

import nltk.corpus
from nltk.stem.porter import PorterStemmer

def Stemming(text):
    porter = PorterStemmer()
    texto=map(porter.stem, text)
    return "".join(list(texto))

def SinStopwords(question):
    question = question.lower()
    lista = list(question)
    simbolos = [",", "¿", "¡", "?", "!", ".", "(", ")", ";", ":"]
    lista2 = filter(lambda x: x not in simbolos, lista)
    question = "".join(lista2)

    # Tokenizamos la pregunta
    token_list = question.split()

    # Eliminando stopwords
    stopwords_list = nltk.corpus.stopwords.words('spanish')
    final_list = [w for w in token_list if not (w in stopwords_list) and len(w)>2]

    return " ".join(final_list)

