#!/usr/bin/env python3
# coding:utf-8
import random
import tkinter


def listToStr(list):
    """ Convertit une liste ["a", "b", "cd"] en un str "abcd" """
    str = ''
    for i in list:
        str += i
    return str


def MixSentence(sentence):
    sentence = sentence.split()
    mxiedSentence = ''
    for word in sentence:
        if not len(word) == 1:
            firstLetter = word[:1]  # on récupère la 1ère lettre du txt
            lastLetter = word[len(word) - 1:]  # et sa dernière
            ponctuation = ''
            while lastLetter == "," or lastLetter == "." or lastLetter == ";" or lastLetter == ":":
                # cas des ponctuations
                ponctuation += lastLetter
                word = word[:len(word)-1]
                lastLetter = word[len(word) - 1:]

            otherLetters = list(word[1:len(word) - 1])  # on récupère les lettres au milieu dans une liste
            random.shuffle(otherLetters)  # qu'on mélange
            otherLetters = listToStr(otherLetters)  # qu'on remet en str
            mxiedWord = firstLetter + otherLetters + lastLetter  # et on assemble le tout
            mxiedSentence += mxiedWord + ponctuation + " "
        else:  # point-virgule et double-point
            mxiedSentence += word + ' '
    return mxiedSentence

print(MixSentence("Ceci est un test avec, des ponctuations ; des appostr'ophes : des choses en tout genre... !! ???"))
